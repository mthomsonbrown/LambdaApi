"""Tests for the version 1 API."""
import requests
import pytest


api_id = 'sitb0jdwm4'
region = 'us-east-2'
deployment = 'prod'
version = 'v1'
route = 'key'
endpoint = 'https://' \
           '{}.execute-api.{}.' \
           'amazonaws.com/{}/{}/{}'.format(api_id, region,
                                           deployment, version, route)

key = 'test_key'
value = 'test_value'


def test_if_tests_work():
    """Pytest is working."""
    working = True
    assert working is True


@pytest.mark.v1
def test_get():
    """GET method returns OK status."""
    response = requests.get(endpoint)
    assert response.status_code is 200, response.text


@pytest.mark.v1
def test_post():
    """POST returns OK status.  For now, this will just echo the request."""
    response = requests.post(
        endpoint,
        json={"key": key, "value": value}
        )
    validate_simple_response(response, key, value)


@pytest.mark.v1
def test_put():
    """PUT returns OK status.  For now, this will just echo the request."""
    response = requests.put(
        endpoint,
        json={"key": key, "value": value}
        )
    validate_simple_response(response, key, value)


@pytest.mark.v1
def test_delete():
    """DELETE returns OK status.  For now, this will just echo the request."""
    response = requests.delete(
        endpoint,
        json={"key": key, "value": value}
        )
    validate_simple_response(response, key, value)


def validate_simple_response(response, key, value):
    """Validate a simple successful response.

    Asserts the response has OK status, and that the key and value are
    mentionded in the text.

    Args:
        response (requests.Response): The response returned from the API call
        key (str): The key field sent in the request
        value (str): The value field sent in the request
    """
    assert response.status_code is 200, response.text
    assert key in response.text
    assert value in response.text
