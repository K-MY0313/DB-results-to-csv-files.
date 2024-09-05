# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
import pandas as pd
import io
from fastapi.responses import Response
from typing import List

# データベース関連のインポート
from .database import get_db
# SQLAlchemyモデルのインポート
from .models import Measurement as MeasurementModel
# Pydanticスキーマのインポート
from .schemas import Measurement as MeasurementSchema
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Reactアプリのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/export/csv")
async def export_csv(db: Session = Depends(get_db)):
    try:
        # データベースからデータを取得
        query = select(MeasurementModel)
        result = db.execute(query).scalars().all()
        
        # PydanticモデルのListに変換
        measurements: List[MeasurementSchema] = [MeasurementSchema.from_orm(item) for item in result]
        
        # DataFrameに変換
        df = pd.DataFrame([m.dict() for m in measurements])
        
        # CSVファイルとして出力
        output = io.StringIO()
        df.to_csv(output, index=False)
        
        return Response(
            output.getvalue(),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=measurements.csv"}
        )
    except Exception as e:
        print(f"Error in export_csv: {str(e)}")  # サーバーログに出力
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")