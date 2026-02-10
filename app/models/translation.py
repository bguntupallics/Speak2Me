from pydantic import BaseModel, Field


class TranslateRequest(BaseModel):
    text: str
    target_language: str = Field(
        ...,
        examples=["es", "fr", "de", "it", "pt", "nl"],
        description="ISO 639-1 language code",
    )
    source_language: str = Field(
        default="en",
        description="ISO 639-1 language code for the source text",
    )


class TranslateResponse(BaseModel):
    original_text: str
    translated_text: str
    source_language: str
    target_language: str
