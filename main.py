import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from infra.models import Weather
from infra.utils import get_weather_context

cities = {}

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """
    Endpoint to render the index.html template.

    Args:
        request (Request): The incoming request object.

    Returns:
        HTMLResponse: Rendered HTML response using the index.html template.
    """
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/weather/{city}", response_model=Weather)
async def get_weather(request: Request, city: str) -> HTMLResponse:
    """
    Fetches weather information for a specific city and renders it in a template.

    This function increments the count of requests for the specified city and
    prepares the weather information context to be rendered in the 'weather.html' template.

    Args:
        request (Request): The incoming request object.
        city (str): The name of the city for which weather information is requested.

    Returns:
        HTMLResponse: Rendered HTML response using the 'weather.html' template with the weather context.
    """
    cities[city] = cities[city] + 1 if cities.get(city) else 1
    context = await get_weather_context(city=city)
    return templates.TemplateResponse(request=request, name="weather.html", context=context)


@app.get("/cities")
async def get_cities() -> dict[str, int]:
    """
    Retrieves the current count of requests made for each city.

    Returns:
        dict[str, int]: A dictionary where keys are city names and values are the count of requests made for each city.
    """
    return cities


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
