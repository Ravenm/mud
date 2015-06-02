BASEDIR=$(dirname $0)

cd $BASEDIR/../
gunicorn --config app/gunicorn_settings.py app:app
