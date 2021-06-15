
all:    p328_notes.pdf   p328_notes.html
	echo "notes : done."

%.pdf : %.tex
	pdflatex $*.tex
	pdflatex $*.tex
	pdflatex $*.tex

# Latex2HTML
NOTES = ./p328_notes
VPATH = $(NOTES)

p328_notes.html: p328_notes.tex   .latex2html-init
	pdflatex p328_notes.tex
	pdflatex p328_notes.tex
	pdflatex p328_notes.tex
	latex2html -dir $(NOTES) p328_notes.tex
	./add_yaml.py head.yaml p328_notes

clean:
	if [ -d $(NOTES) ] ; then \
		rm -r $(NOTES)/*; \
		else true; \
	fi;
	rm -f *.dvi *.aux *.log *.out *.pdf
	echo "notes : clean.";echo
