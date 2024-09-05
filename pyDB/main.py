import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from sqlalchemy.orm import Session
from pyDB import models, database
from datetime import datetime

# LabVIEWとの連携用関数
def update_measurement(data1, data2, data3):
    db = database.SessionLocal()
    value = data1 + data2 + data3
    new_measurement = models.Measurement(
            timestamp=datetime.now(),
            value1=float(data1),
            value2=float(data2),
            value3=float(data3)
        )
    db.add(new_measurement)
    db.commit()
    db.close()
        # db.refresh(new_measurement)  # この行をコメントアウトまたは削除
    return value
        