from flashsim import FlashSimulator

def main():
    print("SanDisk Flash Storage Simulator")
    print("=" * 65)

    simulator = FlashSimulator(blocks=8, pages_per_block=8, seed=42)
    simulator.run_workload(operations=100, logical_pages=16)

    print("\nLogical-to-Physical Mapping")
    print("-" * 40)
    for logical, physical in simulator.ftl.mapping_snapshot().items():
        print(f"LPN {logical:02d} -> Block {physical[0]}, Page {physical[1]}")

    simulator.report()

if __name__ == "__main__":
    main()
