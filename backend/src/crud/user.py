from typing import Type

from core.security import get_password_hash
from fastapi import HTTPException, status
from models.user import User
from schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from utils.notifications import send_email_notification
from utils.validators import user_email_exists


def create_user():
    pass


def update_email():
    pass


def get_by_id():
    pass
