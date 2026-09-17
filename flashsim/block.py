from dataclasses import dataclass, field
from .page import Page

@dataclass
class Block:
    block_id: int
    pages_per_block: int
    erase_count: int = 0
    pages: list[Page] = field(init=False)

    def __post_init__(self) -> None:
        self.pages = [Page(self.block_id, i) for i in range(self.pages_per_block)]

    def free_page(self) -> Page | None:
        for page in self.pages:
            if not page.valid and page.data is None:
                return page
        return None

    def valid_pages(self) -> list[Page]:
        return [p for p in self.pages if p.valid]

    def invalid_pages(self) -> list[Page]:
        return [p for p in self.pages if not p.valid and p.data is not None]

    def free_pages(self) -> list[Page]:
        return [p for p in self.pages if not p.valid and p.data is None]

    def is_full(self) -> bool:
        return self.free_page() is None

    def erase(self) -> None:
        self.erase_count += 1
        for page in self.pages:
            page.logical_page = None
            page.data = None
            page.valid = False
