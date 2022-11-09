# build a schema using pydantic
from pydantic import BaseModel


class Servers(BaseModel):
    ip: str
    hostname: int
    services: dict

    class Config:
        orm_mode = True
