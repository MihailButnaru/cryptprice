class FakeRequest:
    def __init__(self, status_code: int, data: bytes):
        self._data = data
        self._status_code = status_code

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def content(self) -> bytes:
        return self._data
