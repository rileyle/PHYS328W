all: p328_ref.pdf
	echo "done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex
	cp p328_ref.pdf ../assets/pdf

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "clean.";echo
