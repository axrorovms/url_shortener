make mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

make admin:
	python3 manage.py createsuperuser