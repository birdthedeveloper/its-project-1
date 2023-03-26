
.PHONY: build test 

build: readme
	zip xptace20.zip README.md *.feature

test:
	rm -f output.pdf
	pandoc README.md -o output.pdf
	rm -f output.pdf
	isutf8 *.feature
	isutf8 README.md

readme: README.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o README.pdf
