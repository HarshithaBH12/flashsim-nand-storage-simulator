# Flashsim — NAND Flash Storage Simulator

A Python simulation of core flash-storage concepts designed as a software-engineering portfolio project.

## Features
- NAND flash blocks and pages
- Logical-to-physical address translation (FTL)
- Out-of-place page updates
- Invalid-page tracking
- Garbage collection with victim-block selection
- Page relocation during garbage collection
- Basic wear-leveling analysis
- Performance metrics and write amplification
- Deterministic workload simulation
- Pytest unit tests

## Run

```bash
python3 main.py
```

## Run tests

```bash
pytest -q
```

## Architecture

```text
Workload
   |
   v
FlashSimulator
   |
   +--> FTL --> NANDFlash --> Blocks --> Pages
   |
   +--> Garbage Collector
   |
   +--> Wear Leveling
   |
   +--> Metrics
```

## Resume description

**Flashsim — NAND Flash Storage & FTL Simulator | Python**
- Built a modular NAND flash simulator implementing logical-to-physical address translation, out-of-place updates, invalid-page tracking and block management.
- Implemented garbage collection with valid-page relocation and victim-block selection, plus wear-leveling analysis across flash blocks.
- Added deterministic workload simulation, performance metrics, write-amplification tracking and Pytest unit tests.

## Engineering relevance

The project demonstrates Python software design, modular architecture, testing, Git-ready development, storage-system concepts, reliability metrics and CI/CD readiness.
