python_version=3.5
python_cmd=python${python_version}
current_dir=$(CURDIR)
venv_cmd=${python_cmd} -m venv
virtualenv=. env/bin/activate;
site_packages=env/lib/python${python_version}/site-packages
kivy=${site_packages}/kivy
pythonpath=${current_dir}/${site_packages}

default: install dev-deps

env:
	${venv_cmd} env
	${virtualenv} pip install -U pip
	${virtualenv} pip install -U setuptools

dev-deps:
	${virtualenv} pip install flake8

kivy-deps:
	${virtualenv} pip install Cython --install-option="--no-cython-compile"
	${virtualenv} pip install -r kivy-requirements.txt

${kivy}: kivy-deps
	${virtualenv} pip install -r requirements.txt

install-deps: env ${kivy}

install: env install-deps
	${virtualenv} pip install -e .

app: env
	${virtualenv} python src/main.py

android: env
	${virtualenv} PYTHONPATH=${pythonpath} buildozer -v android debug deploy run

android-release: env
	${virtualenv} PYTHONPATH=${pythonpath} buildozer -v android release deploy run

lint:
	@${virtualenv} flake8 src

clean:
	@rm -rf env bin .buildozer
