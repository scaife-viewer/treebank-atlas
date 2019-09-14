# Treebank Atlas

ATLAS Server for Ancient Greek Treebanks.

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
pip install -r requirements-dev.txt
```

Create a PostgreSQL database `treebank_atlas`:

```
createdb treebank_atlas
```

Populate the database:

```
./manage.py migrate
```

Run the Django dev server:
```
./manage.py runserver
```

Browse to http://localhost:8000/

## Loading data

Create a superuser:

```
./manage.py createsuperuser
```

Run the `import_treebanks` script:

```
python manage.py shell -c 'from treebank_atlas.treebanks.importers import import_treebanks; import_treebanks();'
```

## Sample Queries
