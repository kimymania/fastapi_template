from typing import TYPE_CHECKING

from features.user.models import Users

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from features.user.schemas import UserCreate


async def create_user(data: UserCreate, db: AsyncSession) -> dict:
    user = Users(**data.model_dump())
    db.add(user)
    await db.commit()
    return {"success": "ok"}
