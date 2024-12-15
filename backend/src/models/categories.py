from models.base import Base, BaseMixin
from models.enums import VehicleCategory
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship


class VehicleCategories(Base, BaseMixin):
    vehicle_category = Column(Enum(VehicleCategory), nullable=False)

    vehicles = relationship("Vehicle", back_populates="category")
