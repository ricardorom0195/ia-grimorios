"""General project configuration."""

import os

from typing import Union

from fastapi import FastAPI

from dotenv import load_dotenv

from api.api import router as api_router
from dao.sql import SQL

load_dotenv()

app = FastAPI()

app.include_router(api_router)
SQL.init()

@app.get("/")
def read_root():
    return {"Message": "Welcome to the clover kingdom"}
