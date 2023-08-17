import typing as t
from sqlalchemy import Column, UUID, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
from uuid import uuid4
from datetime import datetime

@as_declarative()
class Base:
    
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement="auto", nullable=False)
    uuid = Column(UUID, index=True, unique=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    last_modified = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)
    