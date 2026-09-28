# Cloud Reliability Lab

A hands-on DevOps and Site Reliability Engineering portfolio project.

The purpose of this project is to build and operate a small application using modern infrastructure and reliability tooling.

## Current Stack

- Python
- FastAPI

## Planned Stack

- Docker
- AWS
- Terraform
- Kubernetes
- Helm
- GitHub Actions
- Prometheus
- Grafana

## Current API Endpoints

### Health

GET /health

Returns the health status of the application.

### Readiness

GET /ready

Returns whether the application is ready to receive traffic.

### Information

GET /info

Returns basic information about the running service.

## Run Locally

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
