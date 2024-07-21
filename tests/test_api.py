import requests


def test_index(url_index):
    response = requests.get(url_index)
    assert response.status_code == 200, f"We expected 200 status code from response, but got {response.status_code}"
    assert "form" in response.text


def test_get_weather(url_weather):
    response = requests.get(f"{url_weather}/Tokyo")
    assert response.status_code == 200, f"We expected 200 status code from response, but got {response.status_code}"
    assert [key in ("temperature", "time", "interval", "wind_speed", "rain") for key in response.text]
