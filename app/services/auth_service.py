from supabase import Client, create_client


class AuthService:
    def __init__(self):
        self.client: Client | None = None

    def init_client(self, supabase_url: str, supabase_key: str):
        """Initialize Supabase client. Called at startup."""
        self.client = create_client(supabase_url, supabase_key)

    def sign_up(self, email: str, password: str):
        return self.client.auth.sign_up({"email": email, "password": password})

    def sign_in(self, email: str, password: str):
        return self.client.auth.sign_in_with_password(
            {"email": email, "password": password}
        )

    def get_user(self, access_token: str):
        return self.client.auth.get_user(access_token)

    def sign_out(self):
        return self.client.auth.sign_out()


auth_service = AuthService()
