import os
import logging
import json
from fastapi import FastAPI


SERVICE_NAME = os.getenv("SERVICE_NAME", "cloud-reliability-lab")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
endpoint="/health"

def log_event(level, message, **fields):
    log_data = {
        "service": SERVICE_NAME,
        "environment": ENVIRONMENT,
        "message": message,
        **fields
    }

    logger.log(level, json.dumps(log_data))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger(SERVICE_NAME)

app = FastAPI(
    title="Cloud Reliability Lab",
    description="A hands-on DevOps/SRE portfolio project.",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "service": SERVICE_NAME,
        "message": "Service is running",
    }


@app.get("/health")
def health():
    log_event(
        logging.INFO,
        "Health check requested",
        endpoint="/health"
    )

    return {
        "status": "ok"
    }


@app.get("/ready")
def ready():
    log_event(
        logging.INFO,
        "Readiness check requested",
        endpoint="/ready"
    )

    return {
        "status": "ready"
    }


@app.get("/info")
def info():
    return {
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }
