from flask import url_for


class TestIndex(object):
    def test_index_page(self, client):
        """first test for index page"""
        response = client.get(url_for('index'))
        assert response.status_code == 200
        assert str(response.data, 'utf-8') == 'Welcome to projectify api'
