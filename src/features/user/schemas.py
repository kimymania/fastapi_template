from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    StringConstraints,
    field_validator,
)

from core.utils import hasher_hash

"""
Pydantic validation constraints
- Usernames are stored as lower case
- Legal special characters for password: ! @ # $ % ^ & * - _ .
"""
USERNAME_PATTERN = r"^[a-zA-Z0-9-_.]+$"
UsernameConstraints = StringConstraints(
    min_length=2,
    max_length=24,
    to_lower=True,
    pattern=USERNAME_PATTERN,
)

PASSWORD_PATTERN = r"^[a-zA-Z0-9!@#$%^&*-_.]+$"  # noqa: S105
PasswordConstraints = StringConstraints(
    min_length=8,
    max_length=16,
    pattern=PASSWORD_PATTERN,
)


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="ignore")


class UserCreate(UserBase):
    username: Annotated[str, UsernameConstraints]
    password: Annotated[str, PasswordConstraints]

    @field_validator("password", mode="after")
    @classmethod
    def hash_password(cls, value: str) -> str:
        return hasher_hash(value)
