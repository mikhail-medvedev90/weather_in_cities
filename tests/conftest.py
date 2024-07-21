import pytest


@pytest.fixture(scope="session")
def port() -> int:
    return 8000


@pytest.fixture(scope="session")
def host() -> str:
    return "localhost"


@pytest.fixture(scope="session")
def url(host, port) -> str:
    return f"http://{host}:{port}"


@pytest.fixture(scope="session")
def url_index(url) -> str:
    return f"{url}/index"


@pytest.fixture(scope="session")
def url_weather(url) -> str:
    return f"{url}/weather"
