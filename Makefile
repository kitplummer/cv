BASENAME=kp-resume
TEMPLATE=readable

all: pdf html

html:
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume html --template $(TEMPLATE) $(BASENAME).md .
pdf:
	docker run -v ${PWD}:/resume there4/markdown-resume md2resume pdf --template $(TEMPLATE) $(BASENAME).md .

pages:
	cp $(BASENAME).html index.html

clean:
	rm kp-resume.html
	rm kp-resume.pdf
