from os import environ
from dotenv import load_dotenv

load_dotenv('.env')


class AppConfig:
    DB_HOST = environ.get('SERVERS_DB_HOST')
    DB_PORT = environ.get('SERVERS_DB_PORT')
    DB_NAME = environ.get('SERVERS_DB_NAME')
    DB_USER = environ.get('SERVERS_DB_USER')
    DB_PASSWORD = environ.get('SERVERS_DB_PASSWORD')
    DB_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)