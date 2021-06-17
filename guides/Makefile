
all:    $(patsubst %.tex,%.pdf,$(wildcard *.tex)) \
	$(patsubst %.tex,%.md,$(wildcard *.tex))
	echo "Guidelines : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex
	pdflatex $*.tex

%.md : %.tex   %.header
	pandoc --mathjax -f latex-auto_identifiers -s $*.header $*.tex  -t markdown-header_attributes -o $*.md

clean:
	rm -f *.dvi *.aux *.log *.out *.pdf *.md
	echo "Guidelines : clean.";echo
