from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)
    # balance = Column(Float)
    # message = Column(String)


class LoginAttempts(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", backref="login_attempts")
    attempt_status = Column(String)
    timestamp = Column(DateTime)


class BlockedUsers(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", backref="blocked_users")
    block_start = Column(DateTime)
    block_end = Column(DateTime)


engine = create_engine("sqlite:///bank.db")
Base.metadata.create_all(engine)
