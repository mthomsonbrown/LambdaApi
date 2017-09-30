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
- Install Python 2.7 and pip following their respective documentation.
- Install pytest: `pip install pytest`

#### Execution:
- Open a terminal and navigate to the `tests` directory.
- To run all tests simply issue the command `pytest`
- To run a specific test, use the `-k` flag in the argument: `pytest -k 'testname'`
- The tests are organized using pytest markers, so if you want to run a subset, use the command: `pytest -m <marker_name>`
  - Currently the supported marker is v1 (`pytest -m v1`)
