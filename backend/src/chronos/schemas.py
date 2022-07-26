from datetime import date

from pydantic import BaseModel


class PricePrediction(BaseModel):
    date: date
    price: float


class PricePredictionResponse(BaseModel):
    status: str
    data: list[PricePrediction]


class PricePredictionRequest(BaseModel):
    coin: str
    interval: str
    forecast_window: int | None
