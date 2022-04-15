import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    DEBUG = True

    mysql_username = os.environ.get('MYSQL_USERNAME')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_dbname = os.environ.get('MYSQL_DBNAME')
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_port = os.environ.get('MYSQL_PORT')

    HASHIDS_KEY = os.environ.get('HASHIDS_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = f'mysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_dbname}'
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
        'css': 'CSS'
    }

    TITLE_MAX_LEN = 128
    EDITOR_MAX_LEN = 16000
