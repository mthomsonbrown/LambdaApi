import pytest
import requests
from requests import codes as status

from test_base import TestBase


@pytest.mark.v2
class TestV2(TestBase):
    """Tests for the version 2 API."""

    def setup_class(cls):
        cls.endpoint = cls.generate_endpoint('v2')

    def test_get_all_items(self):
        """GET method without parameter returns all keys."""
        response = requests.get(self.endpoint)
        assert response.status_code == status.ok, response.status_code
        assert self.valid_value in response.text, response.text

    def test_get_single_item(self):
        """A key can be sent as a path parameter to receive a single value."""
        response = requests.get(self.endpoint + '/' + self.valid_key)
        assert response.status_code == status.ok, response.status_code
        assert self.valid_value in response.text, response.text

    def test_post_unique_item(self):
        """Posting data to a unique key endpoint saves the data."""
        response = requests.post(
            self.endpoint + '/' + self.unique_key(), json=self.test_value)
        assert 'Data saved' in response.text

    def test_post_existing_key(self):
        """Posting an existing key returns an error."""
        response = requests.post(
            self.endpoint + '/' + self.valid_key, json=self.test_value)
        print("Response: " + response.text)
        assert 'An entry for that key already exists' in response.text
        assert response.status_code == status.forbidden

    def test_post_without_parameter(self):
        """Posting without a path parameter returns failure message."""
        response = requests.post(
            self.endpoint, json=self.test_value)
        assert 'Missing path params' in response.text

    def test_post_without_param_returns_error(self):
        """Posting without a path parameter returns HTTP Bad Request."""
        response = requests.post(
            self.endpoint, json=self.test_value)
        assert response.status_code == status.bad_request
