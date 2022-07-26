from datetime import datetime

from pydantic import BaseModel


class BitcoinBlock(BaseModel):
    Block_Height: int
    Date: datetime
    Transaction_Count: int
    Block_Size: float  # in KB
    Block_Weight: int
    Difficulty: int | float  # Some APIs return difficulty as float


class LitecoinBlock(BaseModel):
    Date: datetime
    Block_Time_min: float | None = None
    Transaction_Count: int
    Transaction_Fee_LTC: float | None = None


class BlockchainBlockResponse(BaseModel):
    status: str
    data: list[BitcoinBlock | LitecoinBlock]
