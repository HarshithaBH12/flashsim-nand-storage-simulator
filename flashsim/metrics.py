from dataclasses import dataclass

@dataclass
class Metrics:
    operations: int = 0
    reads: int = 0
    writes: int = 0
    updates: int = 0
    gc_runs: int = 0
    pages_moved: int = 0
    blocks_erased: int = 0

    def record_from(self, ftl, gc) -> None:
        self.reads = ftl.read_count
        self.writes = ftl.write_count
        self.updates = ftl.update_count
        self.gc_runs = gc.gc_runs
        self.pages_moved = gc.pages_moved
        self.blocks_erased = gc.blocks_erased
        self.operations = self.reads + self.writes

    def write_amplification(self) -> float:
        if self.writes == 0:
            return 0.0
        return (self.writes + self.pages_moved) / self.writes

    def report(self) -> None:
        print("\nPERFORMANCE METRICS")
        print("-" * 40)
        print(f"Reads              : {self.reads}")
        print(f"Writes             : {self.writes}")
        print(f"Updates            : {self.updates}")
        print(f"GC Runs            : {self.gc_runs}")
        print(f"Pages Moved        : {self.pages_moved}")
        print(f"Blocks Erased      : {self.blocks_erased}")
        print(f"Write Amplification: {self.write_amplification():.2f}x")
