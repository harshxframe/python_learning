from typing import Optional
from pydantic import BaseModel, Field


class ExampleModel(BaseModel):
    id: int
    name: str = Field(
        ...,
        max_length=100,
        min_length=30,
        description="The id of the employee."
    )
    age:int = Field(
        ge=18,
        le=50
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        le=100000
    )
