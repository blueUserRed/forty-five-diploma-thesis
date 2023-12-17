set LATEX=xelatex

set PANDOCMODULES=markdown+auto_identifiers
set PANDOCMODULES=%PANDOCMODULES%+definition_lists
set PANDOCMODULES=%PANDOCMODULES%+fenced_code_attributes
set PANDOCMODULES=%PANDOCMODULES%+compact_definition_lists
set PANDOCMODULES=%PANDOCMODULES%+autolink_bare_uris
set PANDOCMODULES=%PANDOCMODULES%+pipe_tables+table_captions
set PANDOCMODULES=%PANDOCMODULES%+inline_notes+footnotes+link_attributes+smart


set PANDOCOPT=--listings -N -f %PANDOCMODULES%

cd markdown
for %%f in (*.md) do pandoc %PANDOCOPT% %%f -o "%%f%.tex"
cd ..

cd build

%LATEX% ../diplomarbeit.tex -shell-escape -include-directory=".." -output-directory="../out" -halt-on-error
makeindex -c -q diplomarbeit.idx
bibtex -include-directory=".." diplomarbeit
%LATEX% ../diplomarbeit.tex -shell-escape -include-directory=".." -output-directory="../out" -halt-on-error
%LATEX% ../diplomarbeit.tex -shell-escape -include-directory=".." -output-directory="../out" -halt-on-error

cd ..
