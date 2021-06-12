
all: p328_notes.pdf
	echo "notes : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex
	cp p328_notes.pdf ../assets/pdf

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "notes : clean.";echo
