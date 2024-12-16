from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password: str, hashed_passowrd: str) -> bool:
    raise NotImplementedError


def get_password_hash(password: str) -> str:
    raise NotImplementedError
