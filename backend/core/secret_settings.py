import os

SECRET_KEY = 'django-insecure-aqd$eja4*qlyv0togsmvdg^&+-*bkwsb2f7w2&ztbkgbcoksu2'

SECRET_DB_NAME = os.getenv('DB_NAME')
SECRET_DB_USER = os.getenv('DB_USER')
SECRET_DB_PASSWORD = os.getenv('DB_PASSWORD')
SECRET_DB_HOST = os.getenv('DB_HOST')
SECRET_DB_PORT = os.getenv('DB_PORT')
