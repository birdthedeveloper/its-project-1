
.PHONY: build test 

build: README.pdf
	zip xptace20.zip README.md *.feature

test:
	test -f README.md
	rm -f output.pdf
	pandoc README.md -o output.pdf
	test -f *.feature
	rm -f output.pdf
	isutf8 *.feature
	isutf8 README.md

README.pdf: README.md
	pandoc -V geometry:margin=2cm --variable urlcolor=blue $< -o $@
