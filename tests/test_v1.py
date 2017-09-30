import requests
import pytest

from test_base import TestBase


@pytest.mark.v1
class TestV1(TestBase):
    """Tests for the version 1 API."""

    def setup_class(cls):
        cls.endpoint = cls.generate_endpoint('v1')

    def test_if_tests_work(self):
        """Pytest is working."""
        working = True
        assert working is True

    def test_get(self):
        """GET method returns OK status."""
        response = requests.get(self.endpoint)
        assert response.status_code is 200, response.text

    def test_post(self):
        """POST returns OK status.

        For now, this will just echo the request.
        """
        response = requests.post(
            self.endpoint,
            json={"key": self.valid_key, "value": self.valid_value})
        self.validate_simple_response(
            response, self.valid_key, self.valid_value)

    def test_put(self):
        """PUT returns OK status.

        For now, this will just echo the request.
        """
        response = requests.put(
            self.endpoint,
            json={"key": self.valid_key, "value": self.valid_value})
        self.validate_simple_response(
            response, self.valid_key, self.valid_value)

    def test_delete(self):
        """DELETE returns OK status.

        For now, this will just echo the request.
        """
        response = requests.delete(
            self.endpoint,
            json={"key": self.valid_key, "value": self.valid_value})
        self.validate_simple_response(
            response, self.valid_key, self.valid_value)

    def validate_simple_response(self, response, key, value):
        """Validate a simple successful response.

        Asserts the response has OK status, and that the key and value are
        mentionded in the text.

        Args:
            response (requests.Response): The response returned from the API
            key (str): The key field sent in the request
            value (str): The value field sent in the request
        """
        assert response.status_code is 200, response.text
        assert key in response.text
        assert value in response.text
