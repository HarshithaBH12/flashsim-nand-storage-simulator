import random
from .flash import NANDFlash
from .ftl import FlashTranslationLayer
from .garbage_collector import GarbageCollector
from .wear_leveling import WearLeveling
from .metrics import Metrics

class FlashSimulator:
    def __init__(self, blocks=8, pages_per_block=8, seed=42):
        self.flash = NANDFlash(blocks, pages_per_block)
        self.ftl = FlashTranslationLayer(self.flash)
        self.gc = GarbageCollector(self.flash, self.ftl)
        self.wear = WearLeveling(self.flash)
        self.metrics = Metrics()
        self.random = random.Random(seed)

    def write(self, logical_page: int, data: str) -> None:
        try:
            self.ftl.write(logical_page, data)
        except RuntimeError:
            if not self.gc.collect():
                raise
            self.ftl.write(logical_page, data)

    def read(self, logical_page: int):
        return self.ftl.read(logical_page)

    def run_workload(self, operations=100, logical_pages=16) -> None:
        for i in range(operations):
            logical_page = self.random.randrange(logical_pages)
            if self.random.random() < 0.75:
                self.write(logical_page, f"data-{i}")
            else:
                self.read(logical_page)
        self.metrics.record_from(self.ftl, self.gc)

    def report(self) -> None:
        self.flash.display()
        print(f"Least worn block : {self.wear.least_worn_block().block_id}")
        print(f"Most worn block  : {self.wear.most_worn_block().block_id}")
        print(f"Wear spread      : {self.wear.wear_spread()}")
        self.metrics.report()
