# Variables
PIPENV = pipenv

# Set up the virtual environment and install dependencies
install:
	$(PIPENV) install

# Make migrations
migrations:
	$(PIPENV) run python manage.py makemigrations

# Apply migrations
migrate:
	$(PIPENV) run python manage.py migrate

# Make and apply migrations
apply_migrations: migrations migrate

# Run tests
test_app:
	$(PIPENV) run python manage.py test

# Run the development server
run: apply_migrations
	$(PIPENV) run python manage.py runserver

# Clean up .pyc files
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Clean up the environment
clean_env:
	$(PIPENV) --rm

# Start a shell in the virtual environment
shell:
	$(PIPENV) shell
