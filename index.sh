NL=$'\n'

mono ../tools/tlister/bin/Release/tlister.exe   -d "" ".tex"   -t "\"" "\""   -t "\lit{" "}"    -t "\lit*{" "}"        -o "keywords.txt"      -e nokeyword.txt          -w "\\lit{{{0}}}"  -s ", \\\\$NL&&\mskip 10mu " 10 -s ", "

mono ../tools/tlister/bin/Release/tlister.exe   -d "" ".tex" -t "\\R{$" "$}{" -o "R.txt" -s ", \\\\{}$NL\mskip 52mu " 2 -s ", " 

mono ../tools/tlister/bin/Release/tlister.exe   -d "" ".tex" -t "\\E{" "}" -o "E.txt" -s ", \\\\{}$NL\mskip 52mu " 5 -s ", " -w "\\langle {0} \\rangle"
