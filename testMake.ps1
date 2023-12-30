$erroractionpreference = "stop"

cd build
rm -r *
cp ../diplomarbeit.tex .
cp ../diplom.bib .
cp ../HTL3RLogo.png .
cp ../HTL3RLogoRGB.eps .
cp -r ../text ./text
xelatex ./diplomarbeit.tex -shell-escape -halt-on-error
cp ./diplomarbeit.pdf ../out
cd ..
