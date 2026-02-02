from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI(title="GitOps CI/CD Demo")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests"
)

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {"status": "ok", "service": "fastapi-gitops"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
