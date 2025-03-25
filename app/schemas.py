from pydantic import BaseModel
from datetime import datetime


class WalletData(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int


class WalletRequestCreate(BaseModel):
    wallet_address: str


class WalletRequestOut(WalletRequestCreate):
    request_time: datetime

    class Config:
        orm_mode = True
