$erroractionpreference = "stop"

cd build

rm -r *
cp ../diplomarbeit.tex .
cp ../diplom.bib .
cp ../HTL3RLogo.png .
cp ../HTL3RLogoRGB.eps .
cp -r ../text ./text
cp -r ../images ./images

xelatex "\def\noMintedCode{}\input{diplomarbeit}" -shell-escape -halt-on-error -output-driver='xdvipdfmx -z3' -no-pdf
makeindex -c -q diplomarbeit.idx
bibtex diplomarbeit
xelatex "\def\noMintedCode{}\input{diplomarbeit}" -shell-escape -halt-on-error -output-driver='xdvipdfmx -z3' -no-pdf
xelatex ./diplomarbeit.tex -shell-escape -halt-on-error -output-driver='xdvipdfmx -z3'
cp ./diplomarbeit.pdf ../out

cd ..
