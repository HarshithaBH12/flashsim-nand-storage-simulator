from dataclasses import dataclass

@dataclass
class Page:
    block_id: int
    page_id: int
    logical_page: int | None = None
    data: str | None = None
    valid: bool = False

    def write(self, logical_page: int, data: str) -> None:
        self.logical_page = logical_page
        self.data = data
        self.valid = True

    def invalidate(self) -> None:
        self.valid = False
