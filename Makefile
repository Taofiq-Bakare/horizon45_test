make_migration:
	python manage.py makemigrations

apply_migration:
	python manage.py migrate

test_app:
	python manage.py test

