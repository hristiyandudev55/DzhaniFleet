from models.base import Base, BaseMixin
from models.enums import DocumentStatus
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class Documents(Base, BaseMixin):
    vehicle_id = Column(ForeignKey("vehicle.id"), nullable=False)
    type_of_document = Column(String, unique=True, nullable=False)
    start_date = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    period_in_days = Column(Integer, nullable=True)
    additional_info = Column(String, nullable=True)
    status = Column(
        Enum(DocumentStatus), nullable=False, default=DocumentStatus.UNKNOWN
    )
    vehicle = relationship("Vehicle", back_populates="documents")
