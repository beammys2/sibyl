from typing import Union

from fastapi import APIRouter, Query

from backend.src.accountant.schemas import (
    AccountInformation,
    ErrorResponse,
    SpotBalanceResponse,
)
from backend.src.exchange_client.exchange_client_factory import ExchangeClientFactory

router = APIRouter(
    prefix="/accountant",
    tags=["Accountant"],
    responses={404: {"description": "Not found"}},
)


@router.get("/account/spot/balance", response_model=Union[SpotBalanceResponse, ErrorResponse])
def get_spot_balance(
    exchange: str = Query(), quote_asset_pair: str = Query(default=None)
) -> SpotBalanceResponse | ErrorResponse:
    client = ExchangeClientFactory.get_client(exchange)
    response = client.get_spot_balance(quote_asset_pair)
    return response


@router.get("/account/information", response_model=Union[AccountInformation, ErrorResponse])
def get_spot_balance(
    exchange: str = Query(),
) -> AccountInformation | ErrorResponse:
    client = ExchangeClientFactory.get_client(exchange)
    response = client.get_account_information()
    return response
