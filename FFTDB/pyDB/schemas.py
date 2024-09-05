from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)