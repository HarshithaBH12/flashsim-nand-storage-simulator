class GarbageCollector:
    def __init__(self, flash, ftl):
        self.flash = flash
        self.ftl = ftl
        self.gc_runs = 0
        self.pages_moved = 0
        self.blocks_erased = 0

    def choose_victim(self) -> int | None:
        candidates = []
        for block in self.flash.blocks:
            valid = len(block.valid_pages())
            invalid = len(block.invalid_pages())
            if invalid > 0:
                candidates.append((valid, block.erase_count, block.block_id))
        if not candidates:
            return None
        return min(candidates)[2]

    def collect(self) -> bool:
        victim_id = self.choose_victim()
        if victim_id is None:
            return False

        victim = self.flash.blocks[victim_id]
        valid_data = [(p.logical_page, p.data) for p in victim.valid_pages()]

        for logical_page, data in valid_data:
            self._relocate(logical_page, data, victim_id)

        self.flash.erase_block(victim_id)
        self.gc_runs += 1
        self.blocks_erased += 1
        return True

    def _relocate(self, logical_page, data, victim_id):
        target = None
        for block in self.flash.blocks:
            if block.block_id == victim_id:
                continue
            target = block.free_page()
            if target is not None:
                break

        if target is None:
            raise RuntimeError("GC could not find a destination page")

        target.write(logical_page, data)
        self.ftl.mapping[logical_page] = (target.block_id, target.page_id)
        self.pages_moved += 1
