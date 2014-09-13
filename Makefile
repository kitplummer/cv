all: pdf html

html:
	md2resume gh-resume.md

pdf:
	md2resume --pdf gh-resume.md

clean:
	rm gh-resume.html
	rm gh-resume.pdf
