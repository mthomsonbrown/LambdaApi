"""These are the handlers that will serve the v1 API."""
from __future__ import print_function


def key_get_handler(event, context):
    """Handle GET requests to the key endpoint.

    This function will return all keys and values that have been entered.
    """
    return "You called GET /key"


def key_post_handler(event, context):
    """Handle POST requests to the key endpoint."""
    return "Trying to add key: {} with value: {}".format(event.get('key'),
                                                         event.get('value'))


def key_put_handler(event, context):
    """Handle PUT requests to the key endpoint."""
    return "Trying to update key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))


def key_delete_handler(event, context):
    """Handle DELETE requests to the key endpoint."""
    return "Trying to delete key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))
