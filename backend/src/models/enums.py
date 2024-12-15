from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class DocumentStatus(str, Enum):
    PAID = "paid"
    EXPIRED = "expired"
