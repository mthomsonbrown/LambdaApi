# AWS Lambda API PoC

This is a demo web service and NoSQL datastore implementation using AWS services to host an API, along with microservice functions and database persistence.

---

## Deployment
This code is designed to be deployed using AWS Lambda and API Gateway services.
- Zip the contents of the `deploy_me` directory.
- Upload each function as a new lambda function in AWS.
- Apply each function to their respective REST methods in API Gateway.

---

## Testing
The included tests can be run to verify the API is working as intended.

#### Setup:
- Install Python 2.7 and pip following their documentation.
- Install pytest: `pip install pytest`

#### Execution:
- Open a terminal and navigate to the `tests` directory.
- To run all tests simply issue the command `pytest`
- To run a specific test, use the `-k` flag in the argument: `pytest -k 'testname'`
- The tests are organized using pytest markers, so if you want to run a subset, use the command: `pytest -m <marker_name>`
  - Example: `pytest -m v2`

---

## Usage
There are two versions available from the endpoints `/v1` and `/v2`.  The `/v1` API is merely a stub outputting test strings for the four HTTP methods I chose to work with: GET, PUT, POST, and DELETE.

This documentation will just cover the `/v2` api, so URLs listed will assume a root URL including `/v2`.


## Show All Keys and Values

Returns a JSON array of all key/value pairs stored in the database.

* **URL**
  /key

* **Method**
  `GET`

* **URL Params**
  None

* **Data Params**
  None

* **Success Response**
  * Code: 200
  * Content: `[{ lambda_api_key: key1, value: value1 }, { lambda_api_key: key2, value: value2 }, ...]`

* **Error Response**
  None

---

## Show Single Key/Value Pair

Returns a JSON object associated with the key specified.

* **URL**
  /key/{key}

* **Method**
  `GET`

* **URL Params**
  **Required:**
  `key=[string]`

* **Data Params**
  None

* **Success Response**
  * Code: 200
  * Content: `{ lambda_api_key: key, value: value }`

* **Error Response**
  * Code: 404
  * Message: "Key [`<key_name>`] not in Database"

---

## Add Key/Value Pair Using Path Parameter

Add a key value pair to the database.  Note, this will only allow new entries to be added.  It does not modify entries if they already exist.

* **URL**
  /key/{key}

* **Method**
  `POST`

* **URL Params**
  **Required**
  `key=[string]` - A new identifier for this data record

* **Data Params**
  **Optional**
  The data for this request can be of any format, but should be URL and JSON safe.  This will get stored verbatim as the value of a new database entry associated with the key provided.

* **Success Response**
  * Code: 200
  * Message: "Data Saved"

* **Error Response**
  * Code: 403
  * Message: "An entry for that key already exists."

---

## Add a Key/Value Pair Using Request Body

Add a key value pair to the database.  Note, this will only allow new entries to be added.  It does not modify entries if they already exist.

* **URL**
  /key

* **Method**
  `POST`

* **URL Params**
  None

* **Data Params**
  **Required**
  `body: { 'key': key, 'value': value }`
  key (string): A new identifier for this data record
  value (any): Data to save in this record

* **Success Response**
  * Code: 200
  * Message: "Data Saved"

* **Error Response**
  * Code: 403
  * Message: "An entry for that key already exists."

---

## Modify an Entry Using Path Parameter

Updates a given key's value with the new value specified.  Note, this will not create a new entry if the key isn't found in the database.  It will only update an existing record.

* **URL**
  /key/{key}

* **Method**
  `PUT`

* **URL Params**
  **Required**
  `key=[string]` - The key for the record you want to change

* **Data Params**
  **Optional**
  The data for this request can be of any format, but should be URL and JSON safe.  This will replace the data currently associated with the specified key.

* **Success Response**
  * Code: 200
  * Message: "Data Saved"

* **Error Response**
  * Code: 403
  * Message: "That key doesn't exist in the database."

---

## Modify an Entry Using Request Body

Updates a given key's value with the new value specified.  Note, this will not create a new entry if the key isn't found in the database.  It will only update an existing record.

* **URL**
  /key

* **Method**
  `PUT`

* **URL Params**
  None

* **Data Params**
  **Required**
  `body: { 'key': key, 'value': value }`
  key (string): The key for the record you want to change
  value (any): Data to save in this record

* **Success Response**
  * Code: 200
  * Message: "Data Saved"

* **Error Response**
  * Code: 403
  * Message: "That key doesn't exist in the database."

---

## Delete Entry

Deletes a specified record.

* **URL**
 /key/{key}

* **Method**
 `DELETE`

* **URL Params**
 **Required**
 `key=[string]` - The key for the record you want to delete

* **Data Params**
  None

* **Success Response**
  * Code: 200
  * Message: "Success"

* **Error Response**
  None
