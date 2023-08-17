from typing import TYPE_CHECKING, List
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database.base_class import Base


if TYPE_CHECKING:
    from .expense import Expense
    from .income import Income

class User(Base):
    first_name = Column(String(255), nullable=False, index=True)
    last_name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)

    #relationships
    expenses = relationship("Expense", back_populates="user")
    incomes = relationship("Income", back_populates="user")

    def __repr__(self) -> str:
        return f"user: {self.first_name} {self.last_name} - email: {self.email}"
    