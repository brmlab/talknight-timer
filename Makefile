

initenv:
	virtualenv .
	virtualenv --relocatable .
	bin/pip install -r requirements.txt
rmenv:
	rm -fr bin lib include local
