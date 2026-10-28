# LLM Hallucination Detection and Mitigation (FINCH-ZK Framework)

> **Academic Research Project — Group 11 (2026)**  
> **Department of Computer Science and Engineering**  
> **Vidya Academy of Science and Technology, Thrissur**

---

## 👥 Project Team & Guide

| Role | Details |
|---|---|
| **Project Title** | **LLM Hallucination Detection and Mitigation** |
| **Framework** | FINCH-ZK (Zero-Knowledge Cross-Model Consistency Framework) |
| **Group Number** | **Group 11** |
| **Team Members** | • **Mohamed Azeem**<br>• **Athul C R**<br>• **Mahi P S**<br>• **Hanock Biju** |
| **Project Guide** | **Ms. Neethu C S**, Assistant Professor, Department of Computer Science and Engineering, Vidya Academy of Science and Technology, Thrissur |
| **Year / Version** | **2026** &bull; Version 2.4.0 Production |

---

## 🌌 System Architecture & FINCH-ZK Engine

```
                             [ User Prompt & Target Response ]
                                             │
                                             ▼
                          [ Stage 1: PySBD Sentence Chunking ]
                                             │
                                             ▼
                 [ Stage 2: Automated Multi-Prompt Variant Generator ]
                    ├── Identity Variant
                    ├── Zero-shot Chain-of-Thought (CoT)
                    ├── Long Answer Variant
                    └── Deep Break-Down Variant
                                             │
                                             ▼
                       [ Stage 3: Cross-Model Reference Sampling ]
                    ├── Anthropic Claude 3.5 Sonnet
                    └── Groq Llama 3.3 70B (Versatile)
                                             │
                                             ▼
                   [ Stage 4: Multi-Threaded Consistency Judge ]
                    ├── ACCURATE (Factually supported)
                    ├── CONTRADICTION (Flagged hallucination)
                    └── NEUTRAL (Subjective / transitional)
                                             │
                                             ▼
                [ Stage 5: Targeted Block Correction & Reflection ]
                    ├── Fine-grained substitution of flawed sentences
                    └── Coherence reflection synthesis
                                             │
                                             ▼
            [ Stage 6: Interactive Visual Analytics & Audit Logging ]
                    ├── Chart.js Factuality & Latency Hub
                    ├── Side-by-Side Diff Comparison Viewer
                    └── JSON / CSV Full Audit Report Downloads
```

---

## 🚀 Key Features

1. **Futuristic Dark-Mode Glassmorphism (`#0B0F19`)**:
   - Ultra-modern cyber aesthetics with neon glowing borders, floating glass cards (`backdrop-blur-xl bg-slate-900/80`), and custom cyber scrollbars.
2. **Admin Authentication**:
   - Secure session-guarded route protection (`admin` / `admin`).
3. **Sentence-Level Block Inspector**:
   - Color-coded badges (`ACCURATE`, `CONTRADICTION`, `NEUTRAL`), confidence meters, detailed explanations, and expandable targeted correction cards.
4. **Interactive Chart.js Analytics Hub**:
   - Factuality distribution doughnut chart.
   - Latency breakdown bar chart profiling PySBD segmentation, sampling, evaluation, and mitigation stages.
   - Real-time token overhead estimation.
5. **Side-by-Side Diff Viewer**:
   - Live comparison between original candidate text and FINCH-ZK synthesized unhallucinated prose.
6. **Audit Report Exporter**:
   - Download complete analysis logs via dedicated `/api/export/json` and `/api/export/csv` endpoints.
7. **Production Zero-Crash Guarantee**:
   - Seamlessly performs live inference with Anthropic Claude & Groq when keys are present, with intelligent fallback validation ensuring high availability under all environments.

---

## 🛠️ Quickstart & Local Setup

### 1. Prerequisites
- Python 3.10+ (Tested on Python 3.13)
- Windows, macOS, or Linux

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/ERYADUKRISHNANNK/LLM-Hallucination-Detection-and-Mitigation.git
cd LLM-Hallucination-Detection-and-Mitigation

# Install dependencies
pip install -r requirements.txt
```

### 3. API Key Configuration (Optional for Live External APIs)
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Add your API credentials:
```env
ANTHROPIC_API_KEY=sk-ant-api03-...
GROQ_API_KEY=gsk_...
FLASK_SECRET_KEY=finch-zk-super-secret-key-2026
```

### 4. Run Application
```bash
# Method A: Direct Python
python app.py

# Method B: One-Click Windows Launcher
run.bat
```
Navigate to **http://localhost:5000** in your browser.

- **Username**: `admin`
- **Password**: `admin`

---

## 🧪 Automated Test Suite
Run the comprehensive 10-step integration suite:
```bash
python test_app.py
```

---

## 📄 License
Academic Research & Development License &copy; 2026 Group 11 &bull; Vidya Academy of Science and Technology.
