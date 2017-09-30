import requests
import pytest

from test_base import TestBase


@pytest.mark.v2
class TestV2(TestBase):
    """Tests for the version 2 API."""

    def setup_class(cls):
        cls.endpoint = cls.generate_endpoint('v2')

    def test_get(self):
        """GET method returns OK status."""
        response = requests.get(self.endpoint)
        assert response.status_code is 200, response.text

    def test_get_path_parameter(self):
        """A key can be sent as a path parameter to recieve a value."""
        response = requests.get(self.endpoint + '/' + self.valid_key)
        assert response.status_code is 200, response.text
        assert self.valid_value in response.text, response.text
