"""Pydantic models from APIS requests."""
from pydantic import BaseModel, Field, field_validator

AFFINITIES = ['Oscuridad', 'Luz', 'Fuego', 'Agua', 'Viento', 'Tierra']

class RegisterSchema(BaseModel):
    """Register student schema."""

    name: str = Field(description="Student name.", max_length=20, min_length=1)
    lastname: str = Field(description="Student lastname.", max_length=20, min_length=1)
    magical_affinity: str = Field(description="Student magical affinity.")
    identidication: str = Field(description="Student lastname.", max_length=10, min_length=1)
    age: int = Field(description="Student age.", gt=0, le=99)

    @field_validator('magical_affinity')
    @classmethod
    def magical_affinity_val(cls, magical_affinity: str) -> str:
        if magical_affinity not in AFFINITIES:
            raise ValueError('Incorrect magic affinity')
        return magical_affinity

class DeleteSchema(BaseModel):
    """Register student schema."""

    approved: bool = Field(description="bool value.")