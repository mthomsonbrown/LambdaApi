import time


class TestBase(object):
    """Common resources for all test suites."""

    api_id = 'sitb0jdwm4'
    region = 'us-east-2'
    deployment = 'prod'
    route = 'key'

    # These are assumed to actually be in the database
    valid_key = 'test_key'
    valid_value = 'Saved Data'
    update_key = 'update_key'

    test_value = {"Test": "JSON content"}

    @classmethod
    def generate_endpoint(cls, version):
        return 'https://{}.execute-api.{}.amazonaws.com/{}/{}/{}'.format(
                    cls.api_id, cls.region, cls.deployment, version, cls.route)

    @classmethod
    def unique_key(cls):
        """Create a key based on the current time that can be used for
        successful post requests.
        """
        return 'test_key_' + str(round(time.time() * 1000))
