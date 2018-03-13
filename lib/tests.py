from flask import json
import pytest


class ViewTestMixin(object):
    """
    Automatically load in a session and client, this is common for a lot of
    tests that work with views.
    """

    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, session, client):
        self.session = session
        self.client = client

    def login(self, email='khaleesi@targaryen.com', password='password'):
        """
        Login a specific user.

        :return: Flask response
        """
        return login(self.client, email, password)


def login(client, email='', password=''):
    """
    Log a specific user in.

    :param client: Flask client
    :param email: The user email
    :type email: str
    :param password: The password
    :type password: str
    :return: Flask response
    """
    user = dict(email=email, password=password)

    data = json.dumps(user)

    response = client.post('/login', headers={'Content-Type': 'application/json'}, data=data)

    j_data = json.loads(response.data)

    return j_data['access_token']
