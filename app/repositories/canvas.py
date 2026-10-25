from core import settings
from redis.asyncio import Redis
from schemas import Pixel


class CanvasRepository:
    CANVAS_KEY = "canvas"
    
    def __init__(self, redis_client: Redis) -> None:
        self._client = redis_client

    async def set_pixel(self, pixel: Pixel) -> None:
        await self._client.hset(self.CANVAS_KEY, f"{pixel.x},{pixel.y}", pixel.color)

    async def all(self) -> list[Pixel]:
        data = await self._client.hgetall(self.CANVAS_KEY)
        pixels = []
        for key, color in data.items():
            x, y = map(int, key.split(","))
            pixel = Pixel(x=x, y=y, color=color)
            pixels.append(pixel)
        return pixels

    async def try_start_cooldown(self, user_id: int) -> bool:
        result = await self._client.set(f"cooldown:{user_id}", 1, nx=True, ex=settings.canvas.cooldown_seconds)
        return result is not None