from pydantic import BaseModel, Field
from typing import Optional


class OrderQueryParameter(BaseModel):
    product_id: Optional[int] = Field(default=None, example=1)
    number: Optional[int] = Field(default=None, example=3)
    user_id: Optional[int] = Field(default=None, example=1)
