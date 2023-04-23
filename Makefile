
.PHONY: build test

build:
	if ! [ "/home/mptacek/r/b/its-project-1/venv/bin/python" = "$$(which python)" ]; then echo venv ; exit 1; fi
	pip freeze > requirements.txt
	zip -r xptace20.zip features requirements.txt

test:
	bash ./run-test.sh
