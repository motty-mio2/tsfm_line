import os
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(servers=[{"url": os.environ["url"], "description": "testing"}])


class message(BaseModel):
    destination: str
    events: list[dict[str, Any]]


@app.post("/webhook")
def webhook(item: message) -> str:
    message: str = item.events[0]["message"]
    print(message)

    return "ok"
