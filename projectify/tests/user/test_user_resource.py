from flask import json
from lib.tests import ViewTestMixin
from projectify.tests.helpers.mock_data \
    import test_correct_user, test_user_username_duplicate, test_user_email_duplicate,\
    test_user_login, test_user_wrong_email, test_user_wrong_password


class TestUserRegistration(ViewTestMixin):
    def test_user_successful_registration(self, client):
        """
        test a user was successfully registered

        :param client: pytest client
        :return:assertion that user was created successfully
        """
        response = client.post('api/v1/register', data=test_correct_user)
        assert response.status_code == 201
        assert 'User created successfully' in str(response.data, 'utf-8')

    def test_user_username_already_taken(self, client):
        """
        test an error is thrown when a user tries to register with a
        username already taken

        :param client: pytest client
        :return: assertion that username was already taken and user was not registered
        """
        response = client.post('api/v1/register', data=test_user_username_duplicate)
        assert response.status_code == 409
        assert 'Username already exist' in str(response.data, 'utf-8')

    def test_user_email_already_taken(self, client):
        response = client.post('api/v1/register', data=test_user_email_duplicate)
        assert response.status_code == 409
        assert 'Email already exist' in str(response.data, 'utf-8')


class TestUserAuthentication(ViewTestMixin):
    def test_auth_successful(self, client):
        data = json.dumps(test_user_login)
        response = client.post('/login', headers={'Content-Type': 'application/json'}, data=data)
        assert response.status_code == 200
        j_data = json.loads(response.data)
        assert j_data['message'] == 'Login successful'

    def test_invalid_email(self, client):
        data = json.dumps(test_user_wrong_email)
        response = client.post('/login', headers={'Content-Type': 'application/json'}, data=data)
        assert response.status_code == 401
        j_data = json.loads(response.data)
        assert 'description' in j_data
        assert j_data['description'] == 'Invalid credentials'
        assert 'error' in j_data
        assert j_data['error'] == 'Bad Request'

    def test_invalid_password(self, client):
        data = json.dumps(test_user_wrong_password)
        response = client.post('/login', headers={'Content-Type': 'application/json'}, data=data)
        assert response.status_code == 401
        j_data = json.loads(response.data)
        assert 'description' in j_data
        assert j_data['description'] == 'Invalid credentials'
        assert 'error' in j_data
        assert j_data['error'] == 'Bad Request'
