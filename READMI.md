# FastAPI Weather App

This project demonstrates a simple FastAPI application that fetches weather data for cities using external APIs and displays it using templates.

## Project Structure

- `main.py`: Contains the main FastAPI application with endpoints for serving HTML templates and fetching weather data.
- `utils.py`: Provides utility functions for geocoding cities and fetching weather data from external APIs.
- `models.py`: Defines data models (`Weather` and `Coordinates`) used throughout the application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/fastapi-weather-app.git
   cd weather_in_cities
   
Install dependencies using pip:
pip install -r requirements.txt

Usage
To run the FastAPI application, use the following command:
uvicorn main:app --reload
This will start the FastAPI server locally, and you can access the endpoints at http://127.0.0.1:8000.

Endpoints
/index: Returns the main HTML page (index.html), where users can select a city.
/weather/{city}: Fetches weather data for the specified city. If the city is not found, an error message is displayed.
/cities: Returns a JSON object containing a count of how many times each city has been queried.

Technologies Used
FastAPI: Web framework used for building APIs with Python.
Jinja2: Template engine for rendering HTML templates.
httpx: HTTP client for making asynchronous requests.
geopy: Library for geocoding and dealing with geographical coordinates.
loguru: Logging library used for logging errors and information.