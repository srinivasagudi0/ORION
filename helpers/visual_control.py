from pydantic import BaseModel, ConfigDict
from typing import Literal

class ScreenStep(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    action: Literal[]
    arguments: dict