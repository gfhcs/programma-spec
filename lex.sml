load "Char";
open Char;

fun separator "," = true
|   separator ";" = true
|   separator "(" = true
|   separator ")" = true
|   separator "{" = true
|   separator "}" = true
|   separator ":" = true
|   separator "[" = true
|   separator "]" = true
|   separator "=" = true
|   separator "'" = true
|   separator _ = false

fun keyword "while" = true
|   keyword "if" = true
|   keyword "else" = true
|   keyword "foreach" = true
|   keyword "handle" = true
|   keyword "in" = true
|   keyword "internal" = true
|   keyword "new" = true
|   keyword "of" = true
|   keyword "return" = true
|   keyword "shared" = true
|   keyword "state" = true
|   keyword "then" = true
|   keyword "try" = true
|   keyword "type" = true
|   keyword "var" = true
|   keyword "void" = true
|   keyword s    = separator s



fun rev l = foldl op:: nil l

datatype state = None | Symbols | Bits | Comment | Word

fun lex None    ((#"'")::cr)         _ = lex Symbols cr nil
|   lex Symbols  ((#"'")::cr)         t = (implode (rev t), cr)
|   lex Symbols  (c::cr)              t = lex Symbols cr (c::t)
|   lex None    ((#"(")::(#"*")::cr) _ = lex Comment cr nil
|   lex Comment ((#"*")::(#")")::cr) t = (implode (rev t), cr)
|   lex Comment (c::cr)              t = lex Comment cr (c::t)
|   lex None    ((#"1")::cr)         _ = lex Bits cr [#"1"]
|   lex None    ((#"0")::cr)         _ = lex Bits cr [#"0"]
|   lex Bits    ((#"1")::cr)         t = lex Bits cr ((#"1")::t)
|   lex Bits    ((#"0")::cr)         t = lex Bits cr ((#"0")::t)
|   lex Bits    cr                   t = (implode (rev t), cr)
|   lex None    (c::cr)              _ = if isSpace c then lex None cr nil else if separator (implode [c]) then (implode [c], cr) else lex Word cr [c]
|   lex Word    (c::cr)              t = if isSpace c orelse separator (implode [c]) then (implode (rev t), c::cr)else lex Word cr (c::t)



fun lex' p = let val (token, rest) = lex None (explode p) nil in (token, implode rest) end

val lex = lex'

val it = ("", "natural + (natural n)	{		try{return calculate(n:toBits(),100)}	handle exception ex{  (* Exception is catched to attach a proper message! *)state new exception('Addition caused an overflow!')	}")

(* Run through the token stream by calling lex (#2it); !*)

