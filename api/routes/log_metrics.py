import pandas as pd

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.params import Form, Body
from fastapi import File, UploadFile
from pydantic import BaseModel

log_metrics_router = APIRouter(prefix="/api/v1", tags=["log_metrics"])

@log_metrics_router.post("/log_metrics/upload_log_file")
async def upload_log_file():
    return JSONResponse({"message": "Upload log file"})

@log_metrics_router.get("/log_metrics/get_log_file")
async def get_log_file():
    return JSONResponse({"message": "Get log file"})

@log_metrics_router.get("/log_metrics/parse_android_log_file")
async def parse_android_log_file():
    df = pd.read_csv("api/data/Andriod/Andriod_2k.log_structured.csv")
    return JSONResponse({"dataframe": df})

@log_metrics_router.get("/log_metrics/parse_apache_log_file")
async def parse_apache_log_file():
    df = pd.read_csv("api/data/Apache/apache_2k.log_structured.csv")
    return JSONResponse({"dataframe": df})