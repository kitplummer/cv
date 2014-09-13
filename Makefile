BASENAME=gh-resume
TEMPLATE=-t gh-template.html

all: pdf html

html:
	md2resume $(TEMPLATE) $(BASENAME).md

pdf:
	md2resume $(TEMPLATE) --pdf $(BASENAME).md

clean:
	rm gh-resume.html
	rm gh-resume.pdf
