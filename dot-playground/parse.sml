load "Char";
load "Int";

fun isSeparator "," = true
|   isSeparator ";" = true
|   isSeparator "(" = true
|   isSeparator ")" = true
|   isSeparator "{" = true
|   isSeparator "}" = true
|   isSeparator ":" = true
|   isSeparator "[" = true
|   isSeparator "]" = true
|   isSeparator "=" = true
|   isSeparator "'" = true
|   isSeparator "?" = true
|   isSeparator _ = false

fun isKeyword "while" = true
|   isKeyword "if" = true
|   isKeyword "else" = true
|   isKeyword "foreach" = true
|   isKeyword "handle" = true
|   isKeyword "in" = true
|   isKeyword "internal" = true
|   isKeyword "new" = true
|   isKeyword "of" = true
|   isKeyword "return" = true
|   isKeyword "shared" = true
|   isKeyword "state" = true
|   isKeyword "then" = true
|   isKeyword "try" = true
|   isKeyword "type" = true
|   isKeyword "var" = true
|   isKeyword "void" = true
|   isKeyword "<>" = true
|   isKeyword "in" = true
|   isKeyword "notin" = true
|   isKeyword "lambda" = true
|   isKeyword s    = isSeparator s

fun essential "in" = true
|   essential "notin" = true
|   essential "=" = true
|   essential "<>" = true
|   essential _ = false

fun rev l = foldl op:: nil l

datatype state = None | Symbols | Bits | Comment | Word

datatype token = I of string | B of string | S of string | K of string | C of string

fun KorI w = if isKeyword w then K w else I w


fun lex None    ((#"'")::cr)          _ = lex Symbols cr nil
|   lex Symbols  ((#"'")::cr)         t = (S (implode (rev t)), cr)
|   lex Symbols  (c::cr)              t = lex Symbols cr (c::t)
|   lex None    ((#"(")::(#"*")::cr)  _ = lex Comment cr nil
|   lex Comment ((#"*")::(#")")::cr)  t = (C (implode (rev t)), cr)
|   lex Comment (c::cr)               t = lex Comment cr (c::t)
|   lex None    ((#"1")::cr)          _ = lex Bits cr [#"1"]
|   lex None    ((#"0")::cr)          _ = lex Bits cr [#"0"]
|   lex Bits    ((#"1")::cr)          t = lex Bits cr ((#"1")::t)
|   lex Bits    ((#"0")::cr)          t = lex Bits cr ((#"0")::t)
|   lex Bits    cr                    t = (B (implode (rev t)), cr)
|   lex None    (c::cr)               _ = if Char.isSpace c then lex None cr nil else if isSeparator (implode [c]) then (K (implode [c]), cr) else lex Word cr [c]
|   lex Word    (c::cr)               t = if Char.isSpace c orelse isSeparator (implode [c]) then (KorI(implode (rev t)), c::cr)else lex Word cr (c::t)
|   lex Word    nil                   t = (KorI(implode (rev t)), nil)



fun tokenize' nil = nil
|   tokenize' cs = case lex None cs nil of (C _, cr) => tokenize' cr | (t, cr) => t :: tokenize' cr

fun tokenize s = tokenize' (explode s)

datatype tree = T of token | N of string * tree list 

fun kNode k = N(k, [T(K k)])
fun iNode i = N("<id>", [T(I i)])
fun bNode b = N("<bits>", [T(B b)])
fun sNode b = N("<symbols>", [T(S b)])

val epsilon = N ("", nil)

fun projectionStart ((B _)::tr) = true
|   projectionStart ((S _)::tr) = true
|   projectionStart ((I _)::tr) = true
|   projectionStart ((K "lambda")::tr) = true
|   projectionStart ((K "(")::tr) = true
|   projectionStart _ = false

fun parameterStart ((I _)::tr) = true
|   parameterStart _ = false

exception Parse of string


fun keyword k ts  = if null ts orelse hd ts <> (K k) then raise Parse "match" else (kNode k, tl ts)

fun extend (ns, ts) nil l = (N(l, ns), ts)
|   extend (ns, ts) (p::pr) l = let val (n , tr) = p ts in extend (ns @ [n], tr) pr l end




fun exp ts = case eq ts of 
	      (n, (K "?")::tr) => extend ([n, kNode("?")], tr) [exp, keyword ":", exp] "<exp>"
	      | (n, tr) => (N("<exp>", [n]), tr)
and eq ts = case ty ts of 
	      (n, (K "=")::tr) => extend ([n, kNode("=")], tr) [exp] "<eq>"
	      | (n, (K "<>")::tr) => extend ([n, kNode("<>")], tr) [exp] "<eq>"
	      | (n, tr) => (N("<eq>", [n]), tr)
and ty ts = case call ts of 
	      (n, (K "in")::tr) => extend ([n, kNode("in")], tr) [typeName] "<ty>"
	      | (n, (K "notin")::tr) => extend ([n, kNode("notin")], tr) [typeName] "<ty>"
	      | (n, tr) => (N("<ty>", [n]), tr)
and call nil = raise Parse "No input left to parse call!"
|   call ((K "new")::tr) = extend ([kNode "new"], tr) [id, call'] "<call>"
|   call ts = extend (nil, ts) [projection, call'] "<call>"
and call' ts = if projectionStart(ts) 
	       then extend (nil, ts) [projection, call'] "<call'>"
	       else (N ("<call'>", [epsilon]), ts)
and projection ts =  extend (nil, ts) [primitive, projection'] "<projection>"
and projection' ((K "[")::tr) =  (case exp tr of 
			    (n, (K ":")::tr) => extend ((kNode "[") :: n :: [kNode ":"], tr) [exp, keyword "]", projection'] "<projection'>"
			   | (n, tr) => extend ((kNode "[") :: [n], tr) [keyword "]", projection'] "<projection'>")
|   projection' ts = (N("<projection'>", [epsilon]), ts)
and primitive ((K "lambda")::tr) = extend ([kNode "lambda"], tr) [parameters, block] "<primitive>"
|   primitive ((K "(")::tr) = extend ([kNode "("], tr) [exp, keyword ")"] "<primitive>"
|   primitive ts = let val (n, tr) = (bits ts handle Parse _ => symbols ts handle Parse _ => id ts) in (N("<primitive>", [n]), tr) end

and parameter ts = extend (nil, ts) [typeName, (fn ((I i)::tr) => (iNode i, tr) | ts => raise Parse "expected identifier!")] "<parameter>"
and parameters ts = if parameterStart(ts) 
	       then extend (nil, ts) [parameter, parameters] "<parameters>"
	       else (N("<parameters>", [epsilon]), ts)
and block ts = extend (nil, ts) [keyword "{", id, keyword "}"] "<block>"

and bits ((B b)::tr) = (bNode b, tr)
|   bits _ = raise Parse "expected: bits"
and symbols ((S b)::tr) = (sNode b, tr)
|   symbols _ = raise Parse "expected: symbols"
and id ((I b)::tr) = (iNode b, tr)
|   id _ = raise Parse "expected: id"
and typeName ((I id)::tr) = (N("<typename>", [iNode id]), tr)
|   typeName _ = raise Parse "expected: type name"


fun parse s = exp (tokenize s) 

exception Error of string
	  	  
fun a1 (T (I s)) = N(s, nil) 
|   a1 (T (B s)) = N(s, nil)  	
|   a1 (T (S s)) = N(s, nil)  	
|   a1 (T (K s)) = N(s, nil)  	
|   a1 (T (C s)) = N(s, nil)
|   a1 (N (l, c)) = 
let
    val R = [("<primitive>", "lambda", "<abs>"),("<call>", "new", "<creation>"),("<eq>", "=", "<eq-pos>"), ("<eq>", "<>", "<eq-neg>"),
			   ("<ty>", "in", "<ty-pos>"), ("<ty>", "notin", "<ty-neg>")]

    exception Found of string
			   
    fun findReplacement c k = foldl (fn ((c', k', r), _) => if c' = c andalso k' = k then raise Found r else NONE ) NONE R handle Found r => SOME r	  


    fun r (l, c) = (case (foldl  (fn (T _, a) => a
				  |  (N (l', _), a) => if isKeyword(l') 
    			      then (case (findReplacement l l', a) of
    			      
    			       (SOME _, SOME _) => raise Error ("Label replacement for category " ^ l ^ " and keyword " ^ l' ^ " is undefined!")
    			     | (NONE, r) => r
    			     | (r, _) => r) else a
    			     )
    			NONE c) of NONE => l | (SOME r) => r)
in
    N(r (l, c), map a1 c)
end
  
fun filter nil = nil
|   filter ((N (l, c))::sr) = if isKeyword l then filter sr else (N(l, c)) :: (filter sr)
|   filter (s::sr) = s :: (filter sr)
  
fun a2 (T n) = T n
|   a2 (N(l, c)) = N(l, map a2 (filter c))

fun a3 (T t) = raise Error "No token label should reach a3!"
|   a3 (N(l, c)) =
let
  val i = N(l, c)
    
  fun leaf (N(l, c)) =  l = "<id>" orelse l = "<bits>" orelse l = "<symbols>" 
  |   leaf _ = raise Error "No token label should reach mayReplace!"
 
  fun essential (T t) = raise Error "No token label should reach mayReplace!"
  |   essential (N(l, c)) = foldl (fn (a, b) => a orelse b) (leaf (N(l, c))) (map essential c)

  exception Double
  
  fun select (i, NONE) = SOME i
  |   select (i, SOME j) = if essential i then 
			    if essential j then raise Double 
			    else SOME i 
			  else SOME j 
			  
  fun getReplacement (N(l, c)) = (foldl select NONE c handle Double => NONE)
  |   getReplacement _ = NONE
  
  fun E (T _) = false
  |   E (N(l, c)) = l = "<creation>" orelse l = "<type>" orelse l = "<abs>"
  
   
in
       if leaf i then i 
  else if E i then N(l,map a3 c)
  else case getReplacement i of 
	    SOME j => a3 j 
	  | NONE   => N(l,map a3 c)
end		

val abstract = a3 o a2 o a1
  
fun tokenToString (I s) = "@Id " ^ s
|   tokenToString (B s) = "@Bt " ^ s	
|   tokenToString (S s) = "@Sb " ^ s	
|   tokenToString (K s) = "@Kw " ^ s	
|   tokenToString (C s) = "@Cm " ^ s	



val (count, reset) = let val c = ref 0
	    in
		(fn () => #1(!c, c := !c +1),
		 fn () => c := 0)
	    end
	    
fun printNode s =  let val id = count() in print (Int.toString(id) ^ " [shape = plaintext, label = \""^ s ^"\"];\n"); id end
		   
		 
fun dot' (T t)  = printNode (tokenToString t)
|   dot' (N(l, c)) = let 
			val c = map dot' c
			val i = printNode l
		    in
		      map (fn j => print (Int.toString(i) ^ " -> " ^ Int.toString(j) ^"\n")) c;
		      i
		    end
		    
fun dot t = let val _ = print "digraph \n{\n"
		val _ = reset()
		val id = dot' t;
	    in
		print "}";
		id
	    end
      
		    
fun test s = 
    let 
	val (s, tr) = parse s
    in    
	print "\nSyntax tree:\n\n\n";
	dot s;
	print "\n\n\nAbstract syntax tree:\n\n\n";
	dot (abstract s);
	print "\n"
    end

test "a[0:1] = f x";
test "lambda bit a bit b {x}";
