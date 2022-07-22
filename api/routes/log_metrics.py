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

# @log_metrics_router.get("/log_metrics/parse_log_file")