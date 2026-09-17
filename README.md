# ⚡ FlashSim — NAND Flash Storage Simulator

> 🐍 A Python-based simulation of NAND flash storage concepts with FTL mapping, garbage collection, wear leveling, performance metrics, automated testing, and CI.

---

## 🚀 Overview

FlashSim is a modular NAND flash storage simulator designed to demonstrate how flash storage manages logical and physical data locations.

It simulates **Logical-to-Physical Mapping, Out-of-Place Updates, Invalid Pages, Garbage Collection, Wear Leveling, and Storage Performance Metrics**.

---

## ✨ Features

- 💾 NAND Flash Blocks & Pages
- 🔄 Logical-to-Physical Address Translation (FTL)
- 📝 Out-of-Place Page Updates
- 🗑️ Invalid Page Tracking
- ♻️ Garbage Collection
- 📦 Valid Page Relocation
- ⚖️ Wear Leveling
- 📊 Performance Metrics
- 📈 Write Amplification Tracking
- 🧪 Pytest Unit Testing
- 🤖 GitHub Actions CI

---

## 🏗️ Architecture

                    📥 Workload
                         │
                         ▼
                🧠 FlashSimulator
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       🔄 FTL      ♻️ Garbage       ⚖️ Wear
          │         Collector       Leveling
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  💾 NAND Flash
                         │
                         ▼
              🧱 Blocks ──► 📄 Pages
                         │
                         ▼
                    📊 Metrics

---

## ▶️ Run

    python3 main.py

---

## 🧪 Run Tests

    pytest -q

---

## 📊 Example Output

    Logical-to-Physical Mapping

    LPN 00 → Block 7, Page 3
    LPN 01 → Block 0, Page 4
    LPN 02 → Block 7, Page 5
    LPN 03 → Block 0, Page 6
    LPN 04 → Block 1, Page 0
    LPN 05 → Block 6, Page 4
    ...

    💾 Storage Statistics

    Blocks          : 8
    Pages/Block     : 8
    Total Pages     : 64
    Valid Pages     : 16
    Invalid Pages   : 42
    Free Pages      : 6

    ⚖️ Wear Statistics

    Least worn block : 2
    Most worn block  : 1
    Wear spread      : 1

    📈 Performance Metrics

    Reads              : 26
    Writes             : 74
    Updates            : 58
    GC Runs            : 2
    Pages Moved        : 0
    Blocks Erased      : 2
    Write Amplification: 1.00x

---

## 🛠️ Tech Stack

🐍 **Python**  
🧪 **Pytest**  
🔧 **Git**  
🐙 **GitHub**  
🤖 **GitHub Actions**

---

## 🎯 Engineering Concepts

💽 NAND Flash Storage  
🔄 Flash Translation Layer (FTL)  
♻️ Garbage Collection  
⚖️ Wear Leveling  
📊 Storage Performance Analysis  
🧪 Automated Testing  
🔁 Git & Version Control  
🤖 Continuous Integration

---

## ⚠️ Note

This project is a software simulation of NAND flash storage behavior. It is intended for learning, experimentation, and demonstrating storage-system concepts through Python.

---

## 👩‍💻 Author

**Harshitha BH**

⭐ Built with Python to simulate how NAND flash storage works internally.
