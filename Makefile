BASENAME=kp-resume
TEMPLATE=-t kp-template.html

all: pdf html

html:
	md2resume $(TEMPLATE) $(BASENAME).md

pdf:
	md2resume $(TEMPLATE) --pdf $(BASENAME).md

pages:
	cp $(BASENAME).html index.html

clean:
	rm kp-resume.html
	rm kp-resume.pdf
