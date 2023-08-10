from _pytest.fixtures import fixture


@fixture(scope="session")
def my_fixture_sample() -> str:
    """:return: a string value representing the sample fixture "MY_FIXTURE"
    """
    return "Test"
