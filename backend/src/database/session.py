from core.config import settings
from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    settings.DATABASE_URL, echo=True, connect_args={"options": "-c timezone=UTC"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Create all tables in the database.
    """
    Base.metadata.create_all(bind=engine)
