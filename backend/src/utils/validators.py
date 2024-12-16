from datetime import timezone
from uuid import UUID

from fastapi import HTTPException
from models.categories import VehicleCategories
from models.enums import Role
from models.users import Users
from sqlalchemy.orm import Session
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)


def user_exists(
    db: Session, user_id: UUID | None = None, user_email: str | None = None
):
    """
    This function checks if user exists by their ID or Email.

    Args:
        db(Session): The database session.
        user_id: The user ID.
        user_email: The email of the user.

    Returns:
        The user instance if found.
    """
    user = None

    if user_id:
        user = db.query(Users).filter(Users.id == user_id).first()
    if user_email:
        user = db.query(Users).filter(Users.email == user_email).first()

    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found!")

    return user


def category_name_unique(db: Session, category_name: str):
    """
    Checks if the category name already exists

    Args:
        db(Session): The database session.
        category_name: The category name to check.

    Raises:
        HTTPException If the category already exists.
    """
    if (
        db.query(VehicleCategories)
        .filter(VehicleCategories.category_name == category_name)
        .first()
    ):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="This category already exists. Please use it.",
        )


def user_email_exists(db: Session, user_email: str):
    """
    Checks if the username already exists.

    Args:
        db(Session): The database session.
        user_email: The email to check.

    Raises:
        HTTPException If the user email already exists.
    """
    if db.query(Users).filter(Users.email == user_email).first():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=(
                "This email is already registered. "
                "If you forgot your password, please select the 'Forgot Password' option."
            ),
        )


def user_is_admin(current_user: Users) -> None:
    """
    Checks if the current user role is admin.

    Args:
        current_user: The user to check.

    Raises:
        HTTPException if the user role is not admin.
    """
    if current_user.role is not Role.ADMIN:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="This action is available only for admins",
        )


def validate_old_vs_new_end_date(old_date, new_date) -> None:
    """
    Validates if the new date is after the old date.

    Args:
        old_date (datetime): The original date of the document.
        new_date (datetime): The new date of creation of the document.

    Raises:
        HTTPException: If the new date is before or the same as the old date.
    """
    old_date = old_date.replace(tzinfo=timezone.utc)
    new_date = new_date.replace(tzinfo=timezone.utc)
    if old_date >= new_date:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="New end date must be after "
            f"{old_date.strftime('%Y-%m-%d %H:%M:%S')}",
        )


def validate_register_num(reg_num: str) -> None:
    """
    Validates if the registration number is valid according to Bulgarian standards.

    Args:
        reg_num (str): The registration number to be validated.

    Raises:
        ValueError: If the registration number is invalid based on Bulgarian format rules.
    """
    pass
