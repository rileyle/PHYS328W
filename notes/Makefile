
all: p328_notes.pdf
	echo "Labs : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "Labs : clean.";echo
