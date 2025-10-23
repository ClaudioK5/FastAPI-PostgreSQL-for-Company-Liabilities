from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class LiabilityItem(Base):
    __tablename__ = "liabilities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Float)
    due_date = Column(String)
    category = Column(String)
    is_paid = Column(Boolean, default=False)

