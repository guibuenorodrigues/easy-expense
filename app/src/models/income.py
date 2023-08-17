from typing import TYPE_CHECKING
from sqlalchemy import Column, String, DateTime, Double, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    from .user import User

class Income(Base):
    description = Column(String(255), nullable=True)
    amount = Column(Double, nullable=False)
    date = Column(DateTime, nullable=False)

    #Foreign Key
    user_id = Column(Integer, ForeignKey("user.id"))

    # relationship
    user = relationship("User", back_populates="incomes")

    def __repr__(self) -> str:
        return f"income on {self.date} - amount: {self.amount}"

