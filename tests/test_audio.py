from app.utils.audio import validate_audio_file


def test_valid_wav():
    assert validate_audio_file("audio/wav", "test.wav", 1024) is None


def test_file_too_large():
    error = validate_audio_file("audio/wav", "test.wav", 30 * 1024 * 1024)
    assert "too large" in error


def test_unsupported_extension():
    error = validate_audio_file("audio/wav", "test.exe", 1024)
    assert "Unsupported" in error


def test_valid_mp3():
    assert validate_audio_file("audio/mpeg", "song.mp3", 5000) is None


def test_no_filename():
    assert validate_audio_file("audio/wav", None, 1024) is None
