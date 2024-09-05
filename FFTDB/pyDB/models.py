from sqlalchemy import Column, Integer, String, DateTime, Date, Interval, ForeignKey,Float
from .database import Base

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    value1 = Column(Float, nullable=False)
    value2 = Column(Float, nullable=False)
    value3 = Column(Float, nullable=False)
   

