from pydantic import BaseModel


class AssetBalance(BaseModel):
    free: float
    locked: float
    price: float


class SpotBalanceResponse(BaseModel):
    spot_balances: dict[str, AssetBalance]


class AccountInformation(BaseModel):
    maker_commission: float  # e.g. 0.1 for 10 BPS
    taker_commission: float
    buyer_commission: float
    seller_commission: float
    can_trade: bool
    can_deposit: bool
    can_withdraw: bool


class ErrorResponse(BaseModel):
    error: str
