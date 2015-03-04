
clean:
	rm -rf data/env
	rm -rf data/flexicadastre/raw/*

data/env/bin/python:
	virtualenv data/env
	data/env/bin/pip install -r data/requirements.txt

flexiscrape: data/env/bin/python
	data/env/bin/python data/flexicadastre/scrape.py

flexiparse: data/env/bin/python
	data/env/bin/python data/flexicadastre/parse.py

flexiload:
	python manage.py loadflexi data/flexicadastre/csv/*

flexi: flexiscrape flexiparse flexiload

migrate:
	python manage.py makemigrations
	python manage.py migrate

web:
	python manage.py runserver
