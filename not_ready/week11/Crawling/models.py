from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class HTTP_links(Base):
    __tablename__ = "HTTP_links"
    id = Column(Integer, primary_key=True, autoincrement=True)
    http_link_name = Column(String)
