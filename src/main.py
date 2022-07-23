import os

import uvicorn
from fastapi import FastAPI

lineapi = os.environ["lineapi"]

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=4040, reload=True)  # type:ignore
