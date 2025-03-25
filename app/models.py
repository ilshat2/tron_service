from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True)
    request_time = Column(DateTime, default=datetime.utcnow)
