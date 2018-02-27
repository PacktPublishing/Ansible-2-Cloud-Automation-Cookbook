FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN FLASK_APP=app.py flask db init
RUN FLASK_APP=app.py flask db migrate
RUN FLASK_APP=app.py flask db upgrade
CMD ["python", "app.py"]
