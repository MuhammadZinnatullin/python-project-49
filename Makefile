install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	 poetry run flake8 brain_games

selfcheck:
	poetry check

check: 
	selfcheck test lint

build: 
	poetry build

brain-games, bg:
	poetry run brain-games

brain-even, be:
	poetry run brain-even

brain-calc, bc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

repackage-install:
	pip install --user --force-reinstall dist/*.whl

asc:
	asciinema rec --overwrite demo.cast
url:
	asciinema upload demo.cast

.PHONY: install test lint selfcheck check build