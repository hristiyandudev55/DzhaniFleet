from models.base import Base, BaseMixin
from models.enums import Role
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class User(Base, BaseMixin):
    pass
