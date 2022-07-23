
from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.params import Form, Body
from fastapi import File, UploadFile
from pydantic import BaseModel

import requests

response_time_router = APIRouter(prefix="/api/v1", tags=["response_time"])

@response_time_router.post("/response_time/calc_response_time")
async def calc_response_time(api_endpoint: str, api_method: str):
    response = requests.request(api_method.uppercase(), api_endpoint)
    elasped_time = response.elapsed.total_seconds()
    return JSONResponse({"response_time": elasped_time})