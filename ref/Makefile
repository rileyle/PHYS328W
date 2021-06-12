all: p328_ref.pdf
	echo "done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "clean.";echo
