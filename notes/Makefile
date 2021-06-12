
all: p328_notes.pdf
	echo "notes : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "notes : clean.";echo
