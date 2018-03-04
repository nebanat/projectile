from lib.tests import ViewTestMixin
from projectify.tests.helpers.mock_users \
    import test_correct_user, test_user_username_duplicate, test_user_email_duplicate


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
