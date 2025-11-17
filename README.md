# 🛡️ Trust & Safety Security Projects

This repository contains **three small yet powerful security and trust-safety projects**. Each project is built using **Python, Machine Learning, and FastAPI**.
They show practical skills useful for **Trust & Safety roles, Cybersecurity Analyst roles, and ML-based content safety systems**.

All projects run locally and use **safe synthetic datasets**.

---

## 📁 Projects Included

### **1️⃣ Content Moderation Engine (Rules + ML)**

This project checks if a message contains harmful content such as:

* toxic language
* threats
* profanity
* suspicious or harmful URLs

It uses:

* a rule-based system (regex patterns)
* a machine learning model to classify messages

API Endpoint:

```
POST /moderate
```

---

### **2️⃣ Fake Account & Bot Detector**

This project detects if a user account looks like a **bot** or **fake account** based on simple profile features:

* number of followers
* number of friends
* number of posts

It uses a **RandomForest** machine learning model.

API Endpoint:

```
POST /predict
```

---

### **3️⃣ Cyber Threat Content Scanner**

This project scans a message and detects:

* phishing-like content
* ransomware or malware mentions
* suspicious URLs
* IP addresses
* file hashes (32–64 characters)

It also uses a small ML model to classify text as **threat** or **normal**.

API Endpoint:

```
POST /scan
```

---

## 🚀 Tech Stack Used

* **Python 3**
* **FastAPI** (for APIs)
* **Scikit-Learn** (for ML models)
* **Pandas**
* **Joblib**
* **Regex for IOC extraction**

---

## 📂 Folder Structure

```
content_moderation/
fake_account_detector/
cyber_threat_scanner/
```

Each folder contains:

```
data/        → datasets
models/      → trained ML models
services/    → helper modules (rules, extractors, utilities)
app/         → API code (FastAPI)
```

---

## ▶️ How to Run Any Project

1. Open the project folder

   ```
   cd content_moderation
   ```

2. Install dependencies

   ```
   pip install -r requirements.txt
   ```

3. Run the API

   ```
   uvicorn app.api:app --reload --port 8000
   ```

4. Test using Postman or curl

Example request:

```
POST /moderate
{
  "text": "This looks suspicious"
}
```

---

## 🔐 Safety Note

All datasets included here are **synthetic and safe**.
They contain no real personal data and do not execute any harmful content.
