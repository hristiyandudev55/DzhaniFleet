from typing import Generator

# Update imports to be relative to src/
from core.authentication import is_token_blacklisted
from core.config import settings
from crud.user import get_by_id
from database.session import SessionLocal
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from schemas.user import UserResponse
from sqlalchemy.orm import Session


def get_db() -> Generator:
    """
    Get a database connection from the connection
    pool and return it to the pool when the request is finished.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> UserResponse:
    """
    Retrieve the current authenticated user based on the provided token.

    Args:
        db (Session): Database session dependency.
        token (str): The JWT token for authentication.

    Returns:
        UserResponse: The authenticated user's response object.

    Raises:
        HTTPException: If the credentials are invalid or the user is logged out.
    """
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    if is_token_blacklisted(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is logged out. Please log in again.",
        )

    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_identifier: str = payload.get("user_id")
        if user_identifier is None:
            raise credential_exception

    except JWTError:
        raise credential_exception

    user = get_by_id(db, str(user_identifier))

    return convert_db_to_user_response(user)


def convert_db_to_user_response(user: User) -> UserResponse:
    """
    Convert a database user object to a user response object.

    Args:
        user (User): The user object from the database.

    Returns:
        UserResponse: The user response object containing the
        user's ID, email, and role.
    """
    return UserResponse(id=user.id, email=user.email, role=user.role)
