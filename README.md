# ⚡ FlashSim — NAND Flash Storage Simulator

> 🐍 A Python-based simulation of core NAND flash storage concepts, including Flash Translation Layer (FTL), garbage collection, wear leveling, performance metrics, automated testing, and CI.

## 🚀 Overview

FlashSim is a modular software simulator that models how NAND flash storage manages data internally.

The project demonstrates how **logical addresses are translated to physical flash pages**, how updates create invalid pages, and how **garbage collection and wear leveling** help manage flash storage efficiently.

## ✨ Features

- 💾 NAND Flash blocks and pages
- 🔄 Logical-to-Physical Address Translation (FTL)
- 📝 Out-of-place page updates
- 🗑️ Invalid-page tracking
- ♻️ Garbage collection with victim-block selection
- 📦 Valid-page relocation during garbage collection
- ⚖️ Wear-leveling analysis
- 📊 Performance metrics
- 📈 Write amplification tracking
- 🔁 Deterministic workload simulation
- 🧪 Pytest unit tests
- 🤖 GitHub Actions CI

## 🏗️ Architecture

```text
📥 Workload
     │
     ▼
🧠 FlashSimulator
     │
     ├── 🔄 FTL
     │     │
     │     ▼
     │   💾 NAND Flash
     │     │
     │     └── 🧱 Blocks → 📄 Pages
     │
     ├── ♻️ Garbage Collector
     │
     ├── ⚖️ Wear Leveling
     │
     └── 📊 Metrics
