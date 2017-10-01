"""These are the handlers that will serve the v2 API."""
from __future__ import print_function

import boto3
import json

# TODO: Use requests module
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_SERVER_ERROR = 500
TABLE_NAME = 'lambda_api_storage'
PRIMARY_KEY = 'lambda_api_key'
VALUE_FIELD = 'value'

dynamo = boto3.resource('dynamodb').Table(TABLE_NAME)


def http_message(message, status=HTTP_INTERNAL_SERVER_ERROR):
    """Formats status messages to send back to the client."""
    return http_response({"message": message}, status)


def http_response(body, status=HTTP_INTERNAL_SERVER_ERROR):
    """Packages response data to send back to the client."""
    return {
        "isBase64Encoded": False,
        "statusCode": status,
        "headers": {"Content-Type": "application/json; charset=UTF-8"},
        "body": json.dumps(body)
    }


def key_get_handler(event, context):
    """Handle GET requests to the key endpoint.

    If a path parameter was included in the url, the specific key value
    pair for that key will be returned.  If the path parameter is not
    included, all key value pairs will be returned.
    """
    if event['pathParameters']:
        key = event['pathParameters']['key']
        result = dynamo.get_item(Key={PRIMARY_KEY: key})
        if 'Item' not in result:
            return http_message(
                "Key [{}] not in Database".format(key), HTTP_NOT_FOUND)
        requested_data = result['Item']
    else:
        result = dynamo.scan()
        if 'Items' not in result:
            return http_message("Database is empty", HTTP_OK)
        requested_data = result['Items']

    return http_response(requested_data, HTTP_OK)


def key_post_handler(event, context):
    """Handle POST requests to the key endpoint.

    Currently this only accepts keys passed as path parameters.  If the key
    already exists, this method will abort.
    """
    if not event['pathParameters']:
        # TODO: serve JSON requests here
        return http_message("Missing path params", HTTP_BAD_REQUEST)

    key = event['pathParameters']['key']

    value = event['body']

    payload = {PRIMARY_KEY: key, VALUE_FIELD: value}
    try:
        dynamo.put_item(
            Item=payload,
            ConditionExpression='attribute_not_exists({})'.format(PRIMARY_KEY))
    # TODO: Catch botocore ConditionalCheckFailedException specifically
    except Exception:
        return http_response(
            "An entry for that key already exists.  "
            + "If you would like to update the value, please "
            + "use the PUT HTTP method",
            HTTP_FORBIDDEN)

    return http_message("Data Saved", HTTP_OK)


def key_put_handler(event, context):
    """Handle PUT requests to the key endpoint."""
    if not event['pathParameters']:
        # TODO: serve JSON requests here
        return http_message("Missing path params", HTTP_BAD_REQUEST)

    key = event['pathParameters']['key']

    value = event['body']

    payload = {PRIMARY_KEY: key, VALUE_FIELD: value}
    try:
        dynamo.put_item(
            Item=payload,
            ConditionExpression='attribute_exists({})'.format(PRIMARY_KEY))
    # TODO: Catch botocore ConditionalCheckFailedException specifically
    except Exception:
        return http_response(
            "That key doesn't exist in the database.  "
            + "If you would like to add the value, please "
            + "use the POST HTTP method",
            HTTP_FORBIDDEN)

    return http_response("Data Saved", HTTP_OK)


def key_delete_handler(event, context):
    """Handle DELETE requests to the key endpoint."""
    if not event['pathParameters']:
        # TODO: serve JSON requests here
        return http_message("Missing path params", HTTP_BAD_REQUEST)

    key = event['pathParameters']['key']
    dynamo.delete_item(Key={PRIMARY_KEY: key})

    return http_message("Success", HTTP_OK)
