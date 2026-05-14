from typing import Annotated

from fastapi import APIRouter, Form

from core.database import SessionDep
from features.user import services
from features.user.schemas import UserCreate

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/create", status_code=201)
async def create_user(data: Annotated[UserCreate, Form(...)], db: SessionDep):
    return await services.create_user(data, db)
