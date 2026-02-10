from unittest.mock import MagicMock, patch

import pytest

from app.services.song_service import SongService


@pytest.mark.asyncio
async def test_search_returns_formatted_results():
    service = SongService()
    mock_sp = MagicMock()
    mock_sp.search.return_value = {
        "tracks": {
            "items": [
                {
                    "name": "Blinding Lights",
                    "artists": [{"name": "The Weeknd"}],
                    "album": {
                        "name": "After Hours",
                        "images": [{"url": "https://example.com/art.jpg"}],
                    },
                    "external_urls": {"spotify": "https://open.spotify.com/track/123"},
                }
            ]
        }
    }
    service.sp = mock_sp

    with patch("app.services.song_service.asyncio.to_thread", side_effect=lambda fn, **kw: fn(**kw)):
        # Call the sync version directly since we're mocking
        import asyncio
        with patch("app.services.song_service.asyncio.to_thread") as mock_thread:
            mock_thread.return_value = mock_sp.search.return_value
            results = await service.search("blinding lights", limit=1)

    assert len(results) == 1
    assert results[0]["title"] == "Blinding Lights"
    assert results[0]["artist"] == "The Weeknd"
    assert results[0]["album"] == "After Hours"
    assert results[0]["spotify_url"] == "https://open.spotify.com/track/123"
