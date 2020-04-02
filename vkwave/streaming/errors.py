class StreamingAPIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.text = message
        self.message = f"[{code}] {message}"
        super().__init__(self.message)
