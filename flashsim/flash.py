from .block import Block

class NANDFlash:
    def __init__(self, num_blocks: int = 8, pages_per_block: int = 8):
        if num_blocks <= 0 or pages_per_block <= 0:
            raise ValueError("Flash dimensions must be positive")
        self.num_blocks = num_blocks
        self.pages_per_block = pages_per_block
        self.blocks = [Block(i, pages_per_block) for i in range(num_blocks)]

    @property
    def total_pages(self) -> int:
        return self.num_blocks * self.pages_per_block

    def allocate_page(self):
        for block in self.blocks:
            page = block.free_page()
            if page is not None:
                return page
        return None

    def valid_page_count(self) -> int:
        return sum(len(b.valid_pages()) for b in self.blocks)

    def invalid_page_count(self) -> int:
        return sum(len(b.invalid_pages()) for b in self.blocks)

    def free_page_count(self) -> int:
        return sum(len(b.free_pages()) for b in self.blocks)

    def erase_block(self, block_id: int) -> None:
        self.blocks[block_id].erase()

    def wear_counts(self) -> list[int]:
        return [b.erase_count for b in self.blocks]

    def display(self) -> None:
        print("=" * 65)
        print(f"Blocks           : {self.num_blocks}")
        print(f"Pages/Block      : {self.pages_per_block}")
        print(f"Total Pages      : {self.total_pages}")
        print(f"Valid Pages      : {self.valid_page_count()}")
        print(f"Invalid Pages    : {self.invalid_page_count()}")
        print(f"Free Pages       : {self.free_page_count()}")
        print(f"Wear Counts      : {self.wear_counts()}")
        print("=" * 65)
