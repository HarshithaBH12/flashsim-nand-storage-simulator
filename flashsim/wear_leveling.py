class WearLeveling:
    def __init__(self, flash):
        self.flash = flash

    def least_worn_block(self):
        return min(self.flash.blocks, key=lambda b: (b.erase_count, b.block_id))

    def most_worn_block(self):
        return max(self.flash.blocks, key=lambda b: (b.erase_count, b.block_id))

    def wear_spread(self) -> int:
        counts = self.flash.wear_counts()
        return max(counts) - min(counts)
