from fastapi import FastAPI

app = FastAPI(
    title="Cloud Reliability Lab",
    description="A hands-on DevOps/SRE portfolio project.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "cloud-reliability-lab",
        "message": "Service is running",
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }


@app.get("/info")
def info():
    return {
        "service": "cloud-reliability-lab",
        "version": "0.1.0",
        "environment": "local",
    }
