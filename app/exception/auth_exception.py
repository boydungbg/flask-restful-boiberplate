class AuthException(Exception):
    code: int
    message: str

    def __init__(self, *args):
        super().__init__(*args)
        self.code = 401
        self.message = "Unauthorize!"
