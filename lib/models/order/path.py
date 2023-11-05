from pydantic import BaseModel, Field
from typing import Optional


class OrderPathParameter(BaseModel):
    order_id: Optional[int] = Field(default=None, example=1)
