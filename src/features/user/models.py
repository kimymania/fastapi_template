from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base, TimestampMixin


class Users(Base, TimestampMixin):
    __tablename__ = "users"

    if TYPE_CHECKING:
        from uuid import UUID

        def __init__(
            self,
            *,
            username: str,
            password: str,
            id: UUID | None = None,
            email: str | None = None,
            displayed_name: str | None = None,
            is_active: bool = True,
            is_admin: bool = True,
        ) -> None: ...

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str | None]
    displayed_name: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
