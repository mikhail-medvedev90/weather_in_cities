import pytest
import requests


@pytest.mark.parametrize("endpoint", ("", "kek", "weather", "index/bug"),
                         ids=("empty_string", "wrong_endpoint", "not_full_endpoint", "broken_endpoint"))
def test_404(url, endpoint):
    response = requests.get(f"{url}/{endpoint}")
    assert response.status_code == 404, f"We expected 404 status code from response, but got {response.status_code}"
    body = response.json()
    assert "detail" in body, f"We expected `detail` from response, but got `{body}`"
    assert body["detail"] == "Not Found", f"`Not Found` must in body, but got `{body}`"
