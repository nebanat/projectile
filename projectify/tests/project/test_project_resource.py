from flask import json
from lib.tests import ViewTestMixin
from projectify.tests.helpers.mock_data import test_project_details, fake_token

fake_headers = {
    'Authorization': 'JWT {}'.format(fake_token)
}


class TestProjectCreation(ViewTestMixin):
    def test_no_token(self, client):
        response = client.post('/api/v1/project', data=test_project_details)
        assert response.status_code == 401
        j_data = json.loads(response.data)
        assert j_data['error'] == 'Authorization Required'
        assert j_data['description'] == 'Request does not contain an access token'

    def test_invalid_token(self, client):
        response = client.post('/api/v1/project', data=test_project_details, headers=fake_headers)
        assert response.status_code == 401
        j_data = json.loads(response.data)
        assert j_data['error'] == 'Invalid token'

    def test_project_successful_creation(self, client):
        token = self.login()
        headers = {
            'Authorization': 'JWT {}'.format(token)
        }
        response = client.post('/api/v1/project', data=test_project_details, headers=headers)
        assert response.status_code == 201
        j_data = json.loads(response.data)
        assert j_data['message'] == 'Project created'

