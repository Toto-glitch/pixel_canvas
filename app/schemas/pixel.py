from typing import Annotated

from core import settings
from pydantic import BaseModel, Field, StringConstraints

HexColor = Annotated[
    str,
    StringConstraints(pattern=r"^#[0-9a-fA-F]{6}$", to_lower=True),
]


class Pixel(BaseModel):
    x: int = Field(ge=0, lt=settings.canvas.width)
    y: int = Field(ge=0, lt=settings.canvas.height)
    color: HexColor
