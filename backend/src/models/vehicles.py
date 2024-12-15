from models.base import Base, BaseMixin
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Vechicle(Base, BaseMixin):
    user_id = Column(ForeignKey("users.id"), nullable=False)
    category_id = Column(ForeignKey("categories.id"), nullable=False)
    registration_num = Column(String(10), nullable=False, unique=True)
    make = Column(String, nullable=True, unique=False)
    model = Column(String, nullable=True, unique=False)
    colour = Column(String, nullable=True, unique=False)
    status = Column(String, nullable=True)
    additional_info = Column(String, nullable=True)

    user = relationship("Users", back_populates="vehicles")
    category = relationship("VehicleCategories", back_populates="vehicles")
    documents = relationship(
        "Documents", back_populates="vehicle", cascade="all, delete-orphan"
    )
