from datetime import timedelta

DEBUG = True

SERVER_NAME = 'localhost:8000'

# SQLAlchemy.
db_uri = 'postgresql://andeladeveloper:root234@postgres:5432/projectify'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = b'\xdb\xec\xf7\xedr\x8b\x1e\x81r\xa4\xe0\x1e\x92\xa7t\xc5\xa6c@\x13'

JWT_AUTH_URL_RULE = '/login'  # override the jwt /auth endpoint
JWT_EXPIRATION_DELTA = timedelta(seconds=1800)  # sets the jwt expiration to 30 mins
JWT_AUTH_USERNAME_KEY = 'email'  # overrides the auth key name with email
