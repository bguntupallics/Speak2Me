# Speak2Me

Voice-driven API that converts spoken commands into structured actions using OpenAI Whisper, with support for translation, song lookup, calculation, and text generation.

## Architecture

- **FastAPI** backend with async endpoints and Pydantic request/response models
- **OpenAI Whisper** (local) for speech-to-text transcription
- **GCP Translation API** for multilingual translation
- **Spotify Web API** for context-aware song search
- **Supabase** for PostgreSQL, authentication (JWT), and real-time APIs

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No | Health check |
| POST | `/audio/transcribe` | Yes | Upload audio file → Whisper → text |
| POST | `/calculator/calculate` | Yes | Natural-language math expression → result |
| POST | `/translation/translate` | Yes | Text + target language → translated text |
| POST | `/songs/search` | Yes | Query → Spotify track results |
| POST | `/transcription/generate` | Yes | Text → downloadable file |
| POST | `/auth/signup` | No | Register with email/password |
| POST | `/auth/login` | No | Login → JWT tokens |
| POST | `/auth/logout` | Yes | Invalidate session |
| GET | `/auth/me` | Yes | Current user profile |
| GET | `/history` | Yes | Paginated command history |

## Setup

### Prerequisites

- Python 3.12+
- ffmpeg (`sudo apt install ffmpeg`)

### API Keys (all free tier)

| Service | Where to get it |
|---------|----------------|
| Supabase | [supabase.com](https://supabase.com) — create a project → get URL + anon key |
| GCP Translation | [console.cloud.google.com](https://console.cloud.google.com) — enable Cloud Translation API → create service account → download JSON key |
| Spotify | [developer.spotify.com](https://developer.spotify.com) — create an app → get client ID + secret |
| Whisper | Runs locally, no key needed |

### Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Edit `.env` with your actual credentials and API keys.

### Supabase Database Setup

Run this SQL in your Supabase SQL editor:

```sql
create table public.command_history (
    id uuid default gen_random_uuid() primary key,
    user_id uuid references auth.users(id) on delete cascade not null,
    command_type text not null check (command_type in (
        'transcribe_audio', 'calculate', 'translate', 'song_search', 'generate_file'
    )),
    input_data jsonb not null default '{}'::jsonb,
    output_data jsonb not null default '{}'::jsonb,
    created_at timestamptz default now() not null
);

create index idx_command_history_user_id on public.command_history(user_id);
create index idx_command_history_type on public.command_history(command_type);

alter table public.command_history enable row level security;

create policy "Users can read own history"
    on public.command_history for select using (auth.uid() = user_id);

create policy "Users can insert own history"
    on public.command_history for insert with check (auth.uid() = user_id);
```

## Running

```bash
source venv/bin/activate
uvicorn main:app --reload
```

API docs available at `http://localhost:8000/docs`.

## Usage Examples

### Calculate

```bash
curl -X POST http://localhost:8000/calculator/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "five times three"}'
```

### Translate

```bash
curl -X POST http://localhost:8000/translation/translate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"text": "Hello world", "target_language": "es"}'
```

### Transcribe Audio

```bash
curl -X POST http://localhost:8000/audio/transcribe \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@recording.wav"
```

### Search Songs

```bash
curl -X POST http://localhost:8000/songs/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"query": "blinding lights", "limit": 5}'
```

## Tests

```bash
source venv/bin/activate
pytest tests/ -v
```

## Project Structure

```
app/
├── config.py            # Pydantic settings, loads .env
├── dependencies.py      # Auth middleware (JWT verification)
├── models/              # Pydantic request/response schemas
├── routers/             # FastAPI route handlers
├── services/            # Business logic + external API wrappers
└── utils/               # Shared helpers (audio validation)
tests/                   # pytest test suite
main.py                  # App entrypoint
```
