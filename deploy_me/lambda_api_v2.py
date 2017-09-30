"""These are the handlers that will serve the v2 API."""
from __future__ import print_function

import boto3

# TODO: Use requests module
HTTP_OK = 200
TABLE_NAME = 'lambda_api_storage'
PRIMARY_KEY = 'lambda_api_key'
VALUE_FIELD = 'value'


def key_get_handler(event, context):
    """Handle GET requests to the key endpoint.

    If a path parameter was included in the url, the specific key value pair
    for that key will be returned.  If the path parameter is not included, all
    key value pairs will be returned.
    """
    dynamo = boto3.resource('dynamodb').Table(TABLE_NAME)

    params = event['pathParameters']
    key = ''
    if params:
        key = params['key']
    if key:
        result = dynamo.get_item(Key={PRIMARY_KEY: key})
    else:
        result = dynamo.scan()
    return {
        'isBase64Encoded': False,
        'statusCode': HTTP_OK,
        'headers': {},
        'body': str(result)
    }


def key_post_handler(event, context):
    """Handle POST requests to the key endpoint."""
    key = event['pathParameters']['key']
    value = event['body']
    dynamo = boto3.resource('dynamodb').Table(TABLE_NAME)
    payload = {PRIMARY_KEY: key, VALUE_FIELD: value}
    result = dynamo.put_item(Item=payload)
    return {
        'isBase64Encoded': False,
        'statusCode': HTTP_OK,
        'headers': {},
        'body': str({
            'message': 'Dynamos response: {}'.format(result)
            })
    }


def key_put_handler(event, context):
    """Handle PUT requests to the key endpoint."""
    return "Trying to update key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))


def key_delete_handler(event, context):
    """Handle DELETE requests to the key endpoint."""
    return "Trying to delete key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))
