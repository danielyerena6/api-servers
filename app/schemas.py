# build a schema using pydantic
from pydantic import BaseModel


class Servers(BaseModel):
    ip: str
    hostname: str

    class Config:
        orm_mode = True
