# ⚡ FlashSim — NAND Flash Storage Simulator

> 🧠 A Python-based simulation of core NAND flash storage concepts, designed as a software-engineering portfolio project.

---

## 🚀 Features

- 💾 **NAND Flash Blocks & Pages**
- 🔄 **Logical-to-Physical Address Translation (FTL)**
- ✏️ **Out-of-Place Page Updates**
- ❌ **Invalid-Page Tracking**
- 🗑️ **Garbage Collection**
- 📦 **Victim-Block Selection**
- 🔁 **Page Relocation During Garbage Collection**
- ⚖️ **Wear-Leveling Analysis**
- 📊 **Performance Metrics**
- 📈 **Write Amplification Tracking**
- 🎯 **Deterministic Workload Simulation**
- 🧪 **Pytest Unit Testing**
- 🤖 **GitHub Actions CI**

---

## 🏗️ Architecture

```text
                    👤 Workload
                        │
                        ▼
                ⚡ Flash Simulator
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       🔄 FTL      🗑️ Garbage      ⚖️ Wear
     Mapping       Collector       Leveling
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 💾 NAND Flash
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          🧱 Blocks            📄 Pages
              │                   │
              └─────────┬─────────┘
                        ▼
                  📊 Metrics
