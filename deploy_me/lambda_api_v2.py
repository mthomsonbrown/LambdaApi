"""These are the handlers that will serve the v2 API."""
from __future__ import print_function

import boto3

# TODO: Use requests module
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_FORBIDDEN = 403
HTTP_INTERNAL_SERVER_ERROR = 500
TABLE_NAME = 'lambda_api_storage'
PRIMARY_KEY = 'lambda_api_key'
VALUE_FIELD = 'value'

# Stub function to populate as a return value from API methods
output = {"isBase64Encoded": False,
          "statusCode": HTTP_INTERNAL_SERVER_ERROR,
          "headers": {'Accept-Encoding': 'UTF-8',
                      'Content-Type': 'application/json'},
          "body": {}
          }


def db_error(message, status=HTTP_INTERNAL_SERVER_ERROR):
    output['statusCode'] = status
    output['body'] = message
    return output


def key_get_handler(event, context):
    """Handle GET requests to the key endpoint.

    If a path parameter was included in the url, the specific key value
    pair for that key will be returned.  If the path parameter is not
    included, all key value pairs will be returned.
    """
    dynamo = boto3.resource('dynamodb').Table(TABLE_NAME)

    params = ''
    key = ''
    params = event['pathParameters']
    if params:
        key = params['key']
        try:
            result = dynamo.get_item(Key={PRIMARY_KEY: key})
        except Exception:
            return db_error('get item failed')
    else:
        try:
            result = dynamo.scan()
        except Exception:
            return db_error('get item failed')

    output['statusCode'] = HTTP_OK
    output['body'] = str(result)
    return output


def key_post_handler(event, context):
    """Handle POST requests to the key endpoint.

    Currently this only accepts keys passed as path parameters.  If the key
    already exists, this method will abort.
    """
    dynamo = boto3.resource('dynamodb').Table(TABLE_NAME)

    key = ''
    if 'pathParameters' not in event:
        return db_error("Missing path params", HTTP_BAD_REQUEST)
    params = event['pathParameters']
    if params:
        key = params['key']
        if not key:
            return db_error("Missing path params", HTTP_BAD_REQUEST)
    else:
        return db_error("Missing key in path params", HTTP_BAD_REQUEST)

    value = event['body']

    payload = {PRIMARY_KEY: key, VALUE_FIELD: value}
    result = {}
    try:
        result = dynamo.put_item(
            Item=payload,
            ConditionExpression='attribute_not_exists({})'.format(PRIMARY_KEY))
    # TODO: Catch botocore ConditionalCheckFailedException specifically
    except Exception:
        output['statusCode'] = HTTP_FORBIDDEN
        output['body'] = str({
            "message": "An entry for that key already exists.  "
                       + "If you would like to update the value, please "
                       + "use the PUT HTTP method"
        })
        return output

    output['statusCode'] = HTTP_OK
    output['body'] = str({"message": "Data saved: {}".format(result)})
    return output


def key_put_handler(event, context):
    """Handle PUT requests to the key endpoint."""
    return "Trying to update key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))


def key_delete_handler(event, context):
    """Handle DELETE requests to the key endpoint."""
    return "Trying to delete key: {} with value: {}".format(event.get('key'),
                                                            event.get('value'))
