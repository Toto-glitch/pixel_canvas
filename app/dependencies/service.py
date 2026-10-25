from typing import Annotated

from core import get_session, redis
from fastapi import Depends
from repositories import CanvasRepository, UserRepository
from services import AuthService, CanvasService
from sqlalchemy.ext.asyncio import AsyncSession


async def get_auth_service(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> AuthService:
    repo = UserRepository(session)
    return AuthService(repo)


def get_canvas_service() -> CanvasService:
    repo = CanvasRepository(redis)
    return CanvasService(repo)
