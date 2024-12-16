from core.security import get_password_hash
from models.users import Users
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from utils.notifications import send_email_notification
from utils.validators import user_email_exists


def create_user(user: UserCreate, db: Session) -> Users:
    user_email_exists(db, user.email)
    hashed_password = get_password_hash(user.password)
    new_user = Users(email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    send_email_notification(
        email=user.email,
        subject="Account Created",
        message="""
        Hi,

        Welcome to DzhaniFleet !

        Your account has been successfully created. You can now log in and start using
        our services.

        If you have any questions, feel free to reach out.

        Best regards,  
        The DzhaniFleet Team
        """,
    )
    return new_user


def update_email():
    pass


def get_by_id():
    pass
