from api.deps import get_current_user, get_db, oauth2_scheme
from core.authentication import authenticate_user, create_access_token
from core.config import settings
from crud.user import create_user, update_email
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User
from schemas.user import (
    Token,
    UserCreate,
    UserRegisterResponse,
    UserUpdate,
)
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    Args:
        user (UserCreate): The user creation data.
        db (Session): Database session dependency.

    Returns:
        UserRegisterResponse: The registered user response object.
    """
    db_user = create_user(user, db)
    return UserRegisterResponse(email=db_user.email, role=db_user.role)


@router.post("/login", include_in_schema=False)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Authenticate a user and return an access token.

    Args:
        form_data (OAuth2PasswordRequestForm):
        The form data containing username and password.
        db (Session): Database session dependency.

    Returns:
        Token: The access token and user information.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(data={"user_id": str(user.id)})
    return Token(
        access_token=access_token,
        token_type="bearer",
        user_id=str(user.id),
        role=user.role,
    )


@router.put("/update")
def update_user(
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update the current user's email.

    Args:
        user (UserUpdate): The user update data.
        db (Session): Database session dependency.
        current_user (User): The current authenticated user.

    Returns:
        str: A message indicating the result of the update operation.
    """
    msg = update_email(db, user.email, current_user)
    return msg


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    """
    Logout the current user by blacklisting their token.

    Args:
        token (str): The token to be blacklisted.

    Returns:
        dict: A message indicating the logout was successful.
    """
    settings.BLACKLISTED_TOKENS.append(token)
    return {"message": "Logout successful."}


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    Retrieve the current authenticated user's details.

    Args:
        current_user (User): The current authenticated user.

    Returns:
        dict: A dictionary containing the user's ID, email, and role.
    """
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role,
    }
