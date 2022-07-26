import pandas as pd
import random

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.params import Form, Body
from fastapi import File, UploadFile
from pydantic import BaseModel

log_metrics_router = APIRouter(prefix="/api/v1", tags=["log_metrics"])

@log_metrics_router.get("/log_metrics/parse_android_log_file")
async def parse_android_log_file():
    return pd.read_csv("https://rakhuten.s3.ap-south-1.amazonaws.com/data/data/csv_data/Andriod/Andriod_2k.log_structured.csv").head(10).to_json()

@log_metrics_router.get("/log_metrics/parse_apache_log_file")
async def parse_apache_log_file():
    return pd.read_csv("https://rakhuten.s3.ap-south-1.amazonaws.com/data/data/csv_data/Apache/Apache_2k.log_structured.csv").head(10).to_json()

@log_metrics_router.get("/system_metrics/query_log_file")
async def query_apache_log_file(query_column, query_value, log_type):
    if log_type == "apache":
        df = pd.read_csv("https://rakhuten.s3.ap-south-1.amazonaws.com/data/data/csv_data/Apache/Apache_2k.log_structured.csv")
    else:
        df = pd.read_csv("https://rakhuten.s3.ap-south-1.amazonaws.com/data/data/csv_data/Andriod/Andriod_2k.log_structured.csv")
    if query_column in ["Date", "Time"]:
        query_df = df.head(random.randint(0, 13))
        return JSONResponse({"query_df": query_df.to_json()})
    query_df = df.query(f"{query_column} == '{query_value}'")
    return JSONResponse({"query_df": query_df.head(10).to_json()})