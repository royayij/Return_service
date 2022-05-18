##
#  Product Service
#
# @file
# @version 0.1

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	npm install

run: install
	python main.py

db_upgrade: install
	alembic -c daos/migrations/alembic.ini upgrade head

# end
