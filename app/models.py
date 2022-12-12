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

    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname


class Services(Base):
    __tablename__ = "services"
    id = Column(Integer(), index=True, primary_key=True)
    id_server = Column(ForeignKey("servers.id"))
    _type = Column(String())
    vendor = Column(String())
    client = Column(String())
    port = Column(Integer())
    url = Column(String())

    def __int__(self, _type, vendor, client, port, url):
        self._type = _type
        self.vendor = vendor
        self.client = client
        self.port = port
        self.url = url

