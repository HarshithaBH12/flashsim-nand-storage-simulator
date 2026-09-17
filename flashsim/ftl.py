from .flash import NANDFlash

class FlashTranslationLayer:
    """Simple logical-to-physical mapping with out-of-place updates."""

    def __init__(self, flash: NANDFlash):
        self.flash = flash
        self.mapping: dict[int, tuple[int, int]] = {}
        self.read_count = 0
        self.write_count = 0
        self.update_count = 0

    def write(self, logical_page: int, data: str) -> tuple[int, int]:
        if logical_page < 0:
            raise ValueError("Logical page cannot be negative")

        old_location = self.mapping.get(logical_page)
        page = self.flash.allocate_page()

        if page is None:
            raise RuntimeError("No free physical pages. Run garbage collection.")

        page.write(logical_page, data)
        self.mapping[logical_page] = (page.block_id, page.page_id)
        self.write_count += 1

        if old_location is not None:
            self.flash.blocks[old_location[0]].pages[old_location[1]].invalidate()
            self.update_count += 1

        return page.block_id, page.page_id

    def read(self, logical_page: int) -> str | None:
        self.read_count += 1
        location = self.mapping.get(logical_page)
        if location is None:
            return None
        block_id, page_id = location
        page = self.flash.blocks[block_id].pages[page_id]
        return page.data if page.valid else None

    def mapping_snapshot(self) -> dict[int, tuple[int, int]]:
        return dict(sorted(self.mapping.items()))

    def invalidate_mapping(self, logical_page: int) -> None:
        self.mapping.pop(logical_page, None)
