from pydantic import BaseModel
from datetime import datetime

class MeasurementBase(BaseModel):
    timestamp: datetime
    value1: float
    value2: float
    value3: float
    

class MeasurementCreate(MeasurementBase):
    pass

class Measurement(MeasurementBase):
    id: int

    class Config:
        orm_mode = True

# 他のスキーマも必要に応じて追加