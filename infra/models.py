from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Weather:
    """Model weather"""
    temperature_2m: float
    time: str
    interval: int
    wind_speed_10m: float
    rain: float


@dataclass(frozen=True, slots=True)
class Coordinates:
    """Model coordinates"""
    latitude: float
    longitude: float
