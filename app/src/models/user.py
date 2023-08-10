from sqlalchemy import Column, String
from app.database.base_class import Base

class User(Base):
    first_name = Column(String(255), nullable=False, index=True)
    last_name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)