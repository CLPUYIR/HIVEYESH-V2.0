"""
Hyveyesh v2.0: Single endpoint micro-admin API coordinator.
Exposes OpenAI-compatible API for the sub-cluster.
"""

from fastapi import FastAPI

app = FastAPI(title="Hyveyesh Micro-Admin Gateway")

@app.get("/health")
async def health_check():
    return {"status": "online"}

# TODO: Implement llama-server.exe orchestration
