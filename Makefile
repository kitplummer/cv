BASENAME=kp-resume
TEMPLATE=readable

all: pdf html

modern: html-modern pdf-modern

html:
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume html --template $(TEMPLATE) $(BASENAME).md .
pdf:
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume pdf --template $(TEMPLATE) $(BASENAME).md .

pages:
	cp $(BASENAME).html index.html

html-modern:
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume html --template $(TEMPLATE) $(BASENAME).md .
	python3 apply-modern-css.py $(BASENAME).html

pdf-modern: html-modern
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume pdf --template $(TEMPLATE) $(BASENAME).md .

clean:
	rm -f kp-resume.html
	rm -f kp-resume.pdf
	rm -f *.html.bak
