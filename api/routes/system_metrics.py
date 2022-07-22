from linux_metrics import cpu_stat, disk_stat, mem_stat, net_stat
import psutil
from sys import prefix


from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.params import Form, Body
from fastapi import File, UploadFile
from pydantic import BaseModel

from api.utils.network_bandwidth import bytesto

system_metrics_router = APIRouter(prefix="/api/v1", tags=["system_metrics"])

@system_metrics_router.get("/system_metrics/cpu_stat/cpu_info")
async def get_cpu_info():
    return JSONResponse(cpu_stat.cpu_info())

@system_metrics_router.get("/system_metrics/cpu_stat/cpu_times")
async def get_cpu_times():
    return JSONResponse(cpu_stat.cpu_times())

@system_metrics_router.get("/system_metrics/cpu_stat/cpu_percent")
async def get_cpu_percent():
    cpu_idle = cpu_stat.cpu_percents()['idle']
    cpu_usage = 100 - cpu_idle
    return JSONResponse({"cpu_idle": cpu_idle, "cpu_usage": cpu_usage})

@system_metrics_router.get("/system_metrics/cpu_stat/process_running")
async def get_process_running():
    return JSONResponse(cpu_stat.procs_running())

@system_metrics_router.get("/system_metrics/cpu_stat/process_blocked")
async def get_process_blocked():
    return JSONResponse(cpu_stat.procs_blocked())

@system_metrics_router.get("/system_metrics/cpu_stat/cpu_avg_load")
async def get_cpu_avg_load():
    return JSONResponse(cpu_stat.load_avg())

@system_metrics_router.get("/system_metrics/cpu_stat/cpu_info")
async def get_cpu_info():
    return JSONResponse(cpu_stat.cpu_info())

@system_metrics_router.get("/system_metrics/disk_stat/disk_busy")
async def get_disk_utilization():
    return JSONResponse(disk_stat.disk_busy('sda', sample_duration=1))

@system_metrics_router.get("/system_metrics/disk_stat/disk_reads_writes")
async def get_disk_reads_writes():
    r, w = disk_stat.disk_reads_writes('sda1')
    return JSONResponse({"reads": r, "writes": w})

@system_metrics_router.get("/system_metrics/disk_stat/disk_usage")
async def get_disk_usage():
    device, size, used, free, percent, mountpoint = disk_stat.disk_usage('/')
    return JSONResponse({"device": device, "size": size, "used": used, "free": free, "percent": percent, "mountpoint": mountpoint})

@system_metrics_router.get("/system_metrics/disk_stat/disk_reads_writes_per_second")
async def get_disk_reads_writes_per_second():
    r, w = disk_stat.disk_reads_writes_per_second('sda')
    return JSONResponse({"reads": r, "writes": w})

@system_metrics_router.get("/system_metrics/mem_stat/memory_usage")
async def get_memory_usage():
    used, total, _, _, _, _ = mem_stat.mem_stats()
    return JSONResponse({"used": used, "total": total})


@system_metrics_router.get("/system_metrics/net_stat/network_bandwidth_usage")
async def get_network_bandwidth_usage():
    response = psutil.net_io_counters(pernic=True)['lo']
    bytes_sent, bytes_recv = bytesto(response[0], 'm'), bytesto(response[1], 'm')
    return JSONResponse({"bytes_sent": bytes_sent, "bytes_recv": bytes_recv})
    
