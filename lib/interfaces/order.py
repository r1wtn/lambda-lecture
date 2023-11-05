from pydantic import BaseModel, Field


class OrderInterface(BaseModel):
    product_id: int = Field(..., example=1)
    number: int = Field(..., example=3)
    user_id: int = Field(..., example=1)
