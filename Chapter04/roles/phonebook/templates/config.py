import os 

SQLALCHEMY_DATABASE_URI = 'mysql://app:{{ mysql_app_password }}@{{ mysql_host }}/phonebook'
SECRET_KEY = os.urandom(32)
