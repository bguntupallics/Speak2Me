import asyncio

from google.cloud import translate_v2 as translate


SUPPORTED_LANGUAGES = {
    "es": "Spanish", "fr": "French", "de": "German",
    "it": "Italian", "pt": "Portuguese", "nl": "Dutch",
    "ja": "Japanese", "ko": "Korean", "zh": "Chinese",
    "ar": "Arabic", "hi": "Hindi", "ru": "Russian",
}


class TranslationService:
    def __init__(self):
        self.client = None

    def init_client(self):
        """Initialize the GCP Translation client. Called at startup."""
        self.client = translate.Client()

    async def translate(self, text: str, target: str, source: str = "en") -> str:
        if target not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Unsupported target language: {target}. "
                f"Supported: {list(SUPPORTED_LANGUAGES.keys())}"
            )
        result = await asyncio.to_thread(
            self.client.translate, text, target_language=target, source_language=source
        )
        return result["translatedText"]


translation_service = TranslationService()
