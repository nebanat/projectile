from flask import json
from lib.tests import ViewTestMixin
from projectify.tests.helpers.mock_data import test_category_details


class TestCategoryCreation(ViewTestMixin):
    def test_category_with_no_token(self, client):
        response = client.post('/api/v1/category', data=test_category_details)
        assert response.status_code == 401
        j_data = json.loads(response.data)
        assert j_data['error'] == 'Authorization Required'
        assert j_data['description'] == 'Request does not contain an access token'

    def test_category_creation_successful(self, client):
        token = self.login()
        headers = {
            'Authorization': 'JWT {}'.format(token)
        }
        response = client.post('/api/v1/category', data=test_category_details, headers=headers)
        assert response.status_code == 201
        j_data = json.loads(response.data)
        assert j_data['message'] == 'Category created'
        assert j_data['data']['category']['name'] == 'some category'
        assert j_data['data']['category']['slug'] == 'some-category'
        assert j_data['data']['category']['description'] == 'some description'

    def test_category_name_already_taken(self, client):
        token = self.login()
        headers = {
            'Authorization': 'JWT {}'.format(token)
        }
        new_category = {
            'name': 'lawyers'
        }
        response = client.post('/api/v1/category', data=new_category, headers=headers)
        assert response.status_code == 409
        j_data = json.loads(response.data)
        assert j_data['message'] == 'category name already exist'

