from __future__ import annotations

import httpx
from geopy import geocoders
from loguru import logger as log

from infra.models import Coordinates, Weather

gn = geocoders.GeoNames("Misha")


def get_city_coordinates(city: str) -> Coordinates:
    """
    Retrieves the coordinates (latitude and longitude) of a given city using a geocoding service.

    Args:
        city (str): The name of the city for which coordinates are to be fetched.

    Returns:
        Coordinates: A named tuple containing latitude and longitude coordinates of the city.

    Raises:
        AnyException: If there is an error during geocoding or fetching coordinates.

    Notes:
        This function uses an external geocoding service (`gn.geocode`) to fetch coordinates.
        It logs the coordinates retrieved before returning them.
    """
    _, coordinates = gn.geocode(city)
    log.info(coordinates)
    return Coordinates(*coordinates)


async def get_weather_from_external_api(coordinates: Coordinates) -> Weather | None:
    """
    Fetches current weather data from an external API based on given coordinates.

    Args:
        coordinates (Coordinates): The geographic coordinates (latitude and longitude) of the location.

    Returns:
        Weather | None: A Weather object containing current weather data if successful,
                       or None if the API request fails or returns no data.

    Notes:
        This function constructs a URL with the provided coordinates to query an external weather API.
        It uses the `httpx` library for asynchronous HTTP requests.
        Logs the JSON response received from the API for informational purposes.
    """
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={coordinates.latitude}&"
           f"longitude={coordinates.longitude}&current=temperature_2m,wind_speed_10m,rain")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data.get("current", {})
            log.info(data)
            return Weather(**current)
        return None


async def get_weather_context(city: str) -> dict[str, str | Weather | dict]:
    """
    Asynchronously retrieves weather context for a given city.

    Args:
        city (str): The name of the city for which weather context is requested.

    Returns:
        dict[str, str | Weather | dict]: A dictionary containing the weather context.
            - "city" (str): The name of the city.
            - "error" (str): Any error message encountered during the process.
            - "weather" (Weather | dict): Weather data or an empty dictionary if data is not available.

    Notes:
        This function attempts to retrieve the geographic coordinates of the city and fetches current
        weather data from an external API using asynchronous operations.
        If the city does not exist or if there are errors during the process, appropriate error handling
        and logging are implemented to provide feedback.
    """
    context = {"city": city, "error": "", "weather": {}}
    try:
        coordinates = get_city_coordinates(city)
    except TypeError:
        error = f"City: `{city}` does not exist"
        log.exception(error)
        context["error"] = error
    else:
        weather = await get_weather_from_external_api(coordinates)
        context["weather"] = weather
    return context
