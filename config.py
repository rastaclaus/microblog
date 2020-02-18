import os
from pathlib import Path

basedir = Path(__file__).parent.absolute()

class Config:
    SECRET_KEY = 'you-will-newer-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{basedir / "app.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['develop.tema.rastaclaus@gmail.com', 'tema.rastaclaus@gmail.com']
    POSTS_PER_PAGE = 10
