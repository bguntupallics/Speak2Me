import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import audio, auth, calculator, history, songs, transcription, translation
from app.services.auth_service import auth_service
from app.services.history_service import history_service
from app.services.song_service import song_service
from app.services.translation_service import translation_service
from app.services.whisper_service import whisper_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load Whisper model
    whisper_service.model_size = settings.whisper_model_size
    whisper_service.load_model()

    # Init GCP Translation (set credentials path before creating client)
    if settings.gcp_credentials_path:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.gcp_credentials_path
    translation_service.init_client()

    # Init Spotify
    if settings.spotify_client_id and settings.spotify_client_secret:
        song_service.init_client(settings.spotify_client_id, settings.spotify_client_secret)

    # Init Supabase
    if settings.supabase_url and settings.supabase_key:
        auth_service.init_client(settings.supabase_url, settings.supabase_key)
        history_service.init_client(auth_service.client)

    yield


app = FastAPI(
    title="Speak2Me API",
    description="Voice-powered utility API with transcription, translation, calculation, and song search",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(audio.router, prefix="/audio", tags=["Audio Transcription"])
app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
app.include_router(translation.router, prefix="/translation", tags=["Translation"])
app.include_router(songs.router, prefix="/songs", tags=["Song Search"])
app.include_router(transcription.router, prefix="/transcription", tags=["Transcription"])
app.include_router(history.router, prefix="/history", tags=["Command History"])


@app.get("/")
async def health_check():
    return {"status": "ok", "version": "2.0.0"}
