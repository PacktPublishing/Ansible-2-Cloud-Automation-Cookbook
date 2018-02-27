import os

SQLALCHEMY_DATABASE_URI = "mysql://app:{{ rds_admin_pass }}@{{hostvars[groups['tag_Application_cookbook_test'][0]].ansible_host}}/phonebook"
SECRET_KEY = os.urandom(32)
