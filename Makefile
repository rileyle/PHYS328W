
all: p328_notes.pdf p328_ref.pdf \
     $(patsubst lab%.tex,lab%.pdf,$(wildcard lab*.tex))
	echo "Labs : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "Labs : clean.";echo
