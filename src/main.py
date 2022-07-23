from typing import Any
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

from app import line

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "OK"}


class message(BaseModel):
    destination: str
    events: list[dict[str, Any]]


@app.post("/webhook")
def webhook(item: message) -> str:
    message: str = item.events[0]["message"]
    print(message)
    ret = line.message(item=message)

    return ret


if __name__ == "__main__":

    uvicorn.run(app="main:app", host="0.0.0.0", port=5000, reload=True)  # type:ignore
