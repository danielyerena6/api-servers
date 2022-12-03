import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Servers as ModelServers
from schemas import Servers
from schemas import Servers as SchemaServers


app = FastAPI()


@app.get("/")
def root():
    return {
        "state": "Api servers is running...."
    }


if __name__ == "__main__":
    uvicorn.run()
