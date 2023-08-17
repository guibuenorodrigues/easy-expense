from typing import TYPE_CHECKING, List
from sqlalchemy import Column, String, DateTime, Double, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    from .user import User

class Expense(Base):
    description = Column(String(255), nullable=True)
    amount = Column(Double, nullable=False)
    date = Column(DateTime, nullable=False)

    #Foreign Key
    user_id = Column(Integer, ForeignKey("user.id"))

    # relationship
    user = relationship("User", back_populates="expenses")

    def __repr__(self) -> str:
        return f"expense on {self.date} - amount: {self.amount}"

