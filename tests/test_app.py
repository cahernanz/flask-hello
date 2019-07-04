"""Test application."""

import flask
import pytest

from flask_hello.app import app

class TestApp(object):

    @pytest.fixture
    def client(self):
        client = app.test_client()
        yield client

    def test_status_code(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_content(self, client):
        response = client.get('/')
        assert b'Hello World!' in response.data
