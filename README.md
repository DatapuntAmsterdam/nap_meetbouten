Atlas NAP & Meetbouten
======================


Requirements
------------

* Docker-Compose (required)


Developing
----------

Use `docker-compose` to start a local database.

	(sudo) docker-compose start -d

or

	docker-compose up -d

The API should now be available on http://localhost:8100/nap

To run an import, execute:

	./atlas_nap_meetbouten/manage.py run_import


To see the various options for partial imports, execute:

	./atlas_nap_meetbouten/manage.py run_import --help


To import the latest database from acceptance:

	docker exec -it $(docker-compose ps -q database) update-nap.sh

