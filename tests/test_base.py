

class TestBase(object):
    """Common resources for all test suites."""

    api_id = 'sitb0jdwm4'
    region = 'us-east-2'
    deployment = 'prod'
    route = 'key'

    # These are assumed to actually be in the database
    valid_key = 'test_key'
    valid_value = 'test_value'

    @classmethod
    def generate_endpoint(cls, version):
        return 'https://{}.execute-api.{}.amazonaws.com/{}/{}/{}'.format(
                    cls.api_id, cls.region, cls.deployment, version, cls.route)
