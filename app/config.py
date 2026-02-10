from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Supabase
    supabase_url: str = ""
    supabase_key: str = ""

    # GCP Translation
    gcp_project_id: str = ""
    gcp_credentials_path: str = ""

    # Spotify
    spotify_client_id: str = ""
    spotify_client_secret: str = ""

    # Whisper
    whisper_model_size: str = "base"

    # OpenAI (optional, for future use)
    openai_key: str = ""

    # App
    debug: bool = False

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}


settings = Settings()
