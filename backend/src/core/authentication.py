from datetime import datetime, timedelta, timezone
from typing import Type

from core.config import settings
from core.security import verify_password
from fastapi import HTTPException, status
from jose import jwt
from models.users import Users
from sqlalchemy.orm import Session


def authenticate_user():
    pass


def create_access_token():
    pass


def is_token_blacklisted():
    pass
