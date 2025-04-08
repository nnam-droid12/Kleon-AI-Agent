# Kleon AI Agent

![tag : innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)

**Kleon AI Agent** is a modular, multi-agent system designed to assist with financial regulation lookups, anomaly detection, transaction audits, and future personal assistance — all within a scalable, intelligent agent architecture.

---

## 🧠 Agents Overview

| Agent Name               | Address (Endpoint)         | Description                                                                 |
|--------------------------|----------------------------|-----------------------------------------------------------------------------|
| `regulation_lookup_agent` | http://localhost:8001       | Answers questions related to financial regulations based on SEC documents. |
| `anomaly_detection_agent` | http://localhost:8002       | Flags financial anomalies using rule-based analysis.                        |
| `transaction_audit_agent` | http://localhost:8003       | Simulates transaction checks and identifies suspicious entries.            |
| `personal_assistant_agent` *(planned)* | http://localhost:8004 | Aims to help users navigate and query the platform in natural language.     |

All agents are designed to work under the **Innovation Lab** category.

---

## 🚀 Project Goal

To build an extensible AI agent platform for finance-focused automation using language understanding and decentralized agent design.

---

## 🔧 How to Run

```bash
# Clone the repo
git clone https://github.com/nnam-droid12/kleon-ai-agent.git
cd kleon-ai-agent

# Install dependencies
pip install -r requirements.txt

# Run individual agents
python regulation_lookup_agent.py
python anomaly_detection_agent.py
python transaction_audit_agent.py
