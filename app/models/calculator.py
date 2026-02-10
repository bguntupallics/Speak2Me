from pydantic import BaseModel, Field


class CalculateRequest(BaseModel):
    expression: str = Field(
        ...,
        examples=["5 add 3", "10 squared", "27 cube root"],
        description="Natural-language math expression",
    )


class CalculateResponse(BaseModel):
    expression: str
    result: float
    parsed_tokens: list[str | float]
