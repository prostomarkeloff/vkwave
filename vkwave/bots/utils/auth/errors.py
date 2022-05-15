from typing import Dict


class AuthError(Exception):
    def __init__(self, error_object: Dict[str, str]):
        self.error_object = error_object
        self.message = self.error_object['error'].replace('_', ' ').capitalize()
        super(AuthError, self).__init__(self.message)

    def get_error_object(self) -> Dict[str, str]:
        return self.error_object
