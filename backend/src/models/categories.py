from models.base import Base, BaseMixin
from models.enums import VehicleCategory
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship


class VehicleCategories(Base, BaseMixin):
    category_name = Column(Enum(VehicleCategory), nullable=False)

    vehicles = relationship("Vehicle", back_populates="category")
