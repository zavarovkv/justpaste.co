import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    DEBUG = True

    pg_username = os.environ.get('PG_USERNAME')
    pg_password = os.environ.get('PG_PASSWORD')
    pg_dbname = os.environ.get('PG_DBNAME')
    pg_host = os.environ.get('PG_HOST')
    pg_port = os.environ.get('PG_PORT')

    HASHIDS_KEY = os.environ.get('HASHIDS_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = ['en', 'ru', 'eu']
    YA_METRIC_COUNTER = os.environ.get('YA_METRIC_COUNTER')

    PROGRAM_LANGUAGES = {
        'text': 'Plain text',
        'python': 'Python',
        'r': 'R',
        'java': 'Java',
        'c_cpp': 'C/C++',
        'javascript': 'Javascript',
        'html': 'HTML',
        'css': 'CSS',
        'sql': 'SQL'
    }

    TITLE_MAX_LENGTH = 128
    EDITOR_MAX_LENGTH = 16000
