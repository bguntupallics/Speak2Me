from unittest.mock import AsyncMock, patch

import pytest

from app.services.translation_service import TranslationService


@pytest.mark.asyncio
async def test_translate_unsupported_language():
    service = TranslationService()
    service.client = object()  # dummy client
    with pytest.raises(ValueError, match="Unsupported target language"):
        await service.translate("hello", target="zz")


@pytest.mark.asyncio
async def test_translate_calls_client():
    service = TranslationService()

    mock_client = AsyncMock()
    mock_client.translate.return_value = {"translatedText": "hola"}
    service.client = mock_client

    with patch("app.services.translation_service.asyncio.to_thread") as mock_thread:
        mock_thread.return_value = {"translatedText": "hola"}
        result = await service.translate("hello", target="es")
        assert result == "hola"
