import pytest

from config import settings
from projectify.app import create_app
from projectify.extensions import db as _db
from projectify.models import User, Category


@pytest.yield_fixture(scope='session')
def app():
    """
    setup our flask test app, this only gets executed once
    :return: Flask app
    """
    db_uri = '{0}_test'.format(settings.SQLALCHEMY_DATABASE_URI)
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URL': db_uri,
        'JWT_AUTH_URL_RULE': '/login',
        'JWT_AUTH_USERNAME_KEY': 'email'
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test
    :param app: Pytest fixture
    :return: Flask app client
    """

    yield app.test_client()


@pytest.fixture(scope='session')
def db(app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: SQLAlchemy database session
    """
    _db.drop_all()
    _db.create_all()

    # Create a single user because a lot of tests do not mutate this user.
    # It will result in faster tests.
    user_params = {
        'username': 'khaleesi',
        'email': 'khaleesi@targaryen.com',
        'password': 'password'
    }

    category_params = {
        'name': 'lawyers',
        'description': 'some description',
        'slug': 'lawyers'
    }

    test_user = User(**user_params)
    test_user.password = User.encrypt_password(user_params['password'])

    test_category = Category(**category_params)

    _db.session.add(test_user)
    _db.session.add(test_category)
    _db.session.commit()

    return _db


@pytest.yield_fixture(scope='function')
def session(db):
    """
    Allow very fast tests by using rollbacks and nested sessions. This does
    require that your database supports SQL savepoints, and Postgres does.

    Read more about this at:
    http://stackoverflow.com/a/26624146

    :param db: Pytest fixture
    :return: None
    """
    db.session.begin_nested()

    yield db.session

    db.session.rollback()

