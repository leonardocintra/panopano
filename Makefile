install-dev:
	@pip install -r requirements/development.txt

run:
	@python manage.py runserver

shell:
	@python manage.py shell

deploy-prod:
	@git push heroku main
	@git push origin main
	@heroku run python manage.py migrate -- remote prod

deploy-stage:
	@git push stage main
	@heroku run python manage.py migrate --remote stage

deploy-all:
	@git push stage main
	@heroku run python manage.py migrate --remote stage
	@git push prod main
	@heroku run python manage.py migrate --remote prod
	@git push origin main

migrate:
	@python manage.py makemigrations
	@python manage.py migrate

test:
	@python3 manage.py test