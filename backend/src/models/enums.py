from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class DocumentStatus(str, Enum):
    ACTIVE = "active"
    ABOUT_TO_EXPIRE = "about_to_expire"
    EXPIRED = "expired"
    UNKNOWN = "unknown"


class VehicleCategory(str, Enum):
    SNOWPLOW = "snowplow"
    EXCAVATOR = "excavator"
    TRUCK = "truck"
    DUMPER = "dumper"
    CAR = "car"
    BUS = "bus"
    CONSTRUCTION_MACHINERY = "construction_machinery"
    MOTORCYCLE = "motorcycle"
    TRAILER = "trailer"
