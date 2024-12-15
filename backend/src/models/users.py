from models.base import Base, BaseMixin
from models.enums import Role
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import relationship


class Users(Base, BaseMixin):
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default=Role.USER, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)

    vehicles = relationship(
        "Vehicle", back_populates="user", cascade="all, delete-orphan"
    )
