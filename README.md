# 🌐 Website Guard Monitor
**Automated Uptime & Security Heartbeat Tracker**

## 🔍 Overview
This Python tool is designed for **Site Reliability Engineering (SRE)** and **Cybersecurity Monitoring**. It performs real-time checks on web endpoints to ensure availability and logs server responses for forensic auditing.

## 🛠️ Components
* **monitor.py**: The main execution script using `requests` and `urllib3`.
* **site_log.txt**: An automated ledger that stores every connection attempt with a timestamp.

## 🚀 Installation & Usage
1. Clone this repository or download the files.
2. Install dependencies:
   ```bash
   pip install requests

   python monitor.py



🛡️ Why This Is Necessary

In a Cybersecurity context, sudden downtime is often the first sign of a DDoS attack or a server breach. This tool provides:

    Instant Alerts: Know immediately when a service fails.

    Audit Trail: Use site_log.txt to prove exactly when an incident occurred.

    Resilience: Handles SSL errors and connection timeouts without crashing.

---


