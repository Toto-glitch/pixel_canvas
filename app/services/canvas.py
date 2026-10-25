from core import CooldownException
from repositories import CanvasRepository
from schemas import Pixel


class CanvasService:
    def __init__(self, canvas_repo: CanvasRepository) -> None:
        self._canvas = canvas_repo

    async def get_canvas(self) -> list[Pixel]:
        return await self._canvas.all()

    async def place_pixel(self, user_id: int, pixel: Pixel) -> None:
        success = await self._canvas.try_start_cooldown(user_id)
        if not success:
            raise CooldownException()
        await self._canvas.set_pixel(pixel)
