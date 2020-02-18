#! /bin/bash
source flask.env
export MAIL_SERVER=smtp.gmail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export FLASK_APP=microblog.py
export FLASK_ENV=development
flask run
