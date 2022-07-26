from typing import Any

from pydantic import BaseModel


class SpotTradeRequest(BaseModel):
    exchange: str
    order_type: str
    quote_asset: str
    base_asset: str
    side: str
    quantity: float
    price: float | None = None
    stop_price: float | None = None
    take_profit_price: float | None = None
    time_in_force: str | None = None


class SpotTradeResponse(BaseModel):
    status: str
    message: str


class StrategyRequest(BaseModel):
    exchange: str
    quote_asset: str
    quote_amount: float
    base_asset: str
    time_interval: str
    strategy: str
    num_trades: int
    dataset_size: int
    params: dict[str, Any]  # Holds strategy-specific parameters
