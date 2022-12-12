import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import AppConfig
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response

from models import Servers as ModelServers
from schemas import Servers
from schemas import Servers as SchemaServers

engine = create_engine(
    AppConfig.DB_URI
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/servers")
def all_servers(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit

    servers = db.query(ModelServers).group_by(ModelServers.id).limit(limit).offset(skip).all()
    return {'code': 200, 'message': "Servers list success", 'data': servers}


@app.post('/servers', status_code=status.HTTP_201_CREATED)
def insert_servers(servers: SchemaServers, db: Session = Depends(get_db)):
    input_server = servers.dict()
    server = ModelServers(ip=input_server["ip"], hostname=input_server["hostname"])
    db.add(server)
    db.commit()
    db.close()

    return {"code": 201, "message": "Server insert successfull", "data": servers}





    return {'code': 201, 'message': 'All servers inserted', 'data': servers}


@app.get("/")
def root():
    return {
        "state": "Api servers is running...."
    }


if __name__ == "__main__":
    uvicorn.run()
