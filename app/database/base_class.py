import typing as t
from sqlalchemy import Column, UUID, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import as_declarative
from uuid import uuid4
from datetime import datetime

class_registry: t.Dict = {}

@as_declarative(class_registry=class_registry)
class Base:
    __name__: str
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement="auto", nullable=False)
    uuid = Column(UUID, index=True, unique=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    last_modified = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()