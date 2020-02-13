import os
from pathlib import Path

basedir = Path(__file__).parent.absolute()

class Config:
    SECRET_KEY = 'you-will-newer-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            f'sqlite:/{ basedir / "app.db" }'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
