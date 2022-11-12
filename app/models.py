from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, JSON, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Servers(Base):
    __tablename__ = "servers"
    id = Column(Integer(), index=True, primary_key=True)
    ip = Column(String(15))
    hostname = Column(String())
    services = Column(JSON)

    def __init__(self, ip, hostname, services):
        self.ip = ip
        self.hostname = hostname
        self.services = services
