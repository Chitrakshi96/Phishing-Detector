# Phishing Detector
# 🛡️ Simple AI Phishing Detector

A beginner-friendly machine learning project that uses a **Random Forest Classifier** to predict whether a URL is **safe** or a **phishing attempt** — based on simple URL features like length, dot count, and hyphens.

---

## 👤 Author

| Field | Details |
|-------|---------|
| **Name** | Chitrakshi Chauhan |
| **Registration No.** | 25BAI11264 |
| **Branch** | Computer Science & Engineering |
| **University** | VIT Bhopal University |

---

## 📌 Project Overview

This project demonstrates a simple AI-powered phishing URL detector built using Python and `scikit-learn`. It trains a Random Forest model on a small labeled dataset of safe and phishing URLs, then allows the user to input any URL and get an instant prediction.

> **No prior ML experience needed** — the code is fully commented and beginner-friendly.

---

## 🧠 How It Works

The model analyzes 3 features extracted from a URL:

| Feature | Description | Example (`secure-login-bank.net`) |
|---------|-------------|----------------------------------|
| `length` | Total character count of the URL | 21 |
| `dots` | Number of `.` in the URL | 1 |
| `hyphen` | Whether the URL contains a `-` | 1 (Yes) |

These features are fed into a **Random Forest Classifier** which predicts:
- `✅ SAFE` — likely a legitimate website
- `⚠️ PHISHING` — likely a phishing/malicious URL

---

## 📁 Project Structure

```
phishing-detector/
│
├── phishing_detector.py   # Main script
└── README.md              # Project documentation
```

---

## ⚙️ Requirements

- Python 3.7+
- pandas
- scikit-learn

Install dependencies with:

```bash
pip install pandas scikit-learn
```

---

## 🚀 How to Run

```bash
python phishing_detector.py
```

You will see:

```
--- 🛡️ Simple AI Phishing Detector ---
Enter a URL to check: verify-update-paypal.com
Prediction: ⚠️ PHISHING
```

---

## 🧪 Sample Test URLs

| URL | Expected Result |
|-----|----------------|
| `google.com` | ✅ SAFE |
| `github.com` | ✅ SAFE |
| `secure-login-bank.net` | ⚠️ PHISHING |
| `win-free-giftcard.biz` | ⚠️ PHISHING |
| `verify-update-paypal.com` | ⚠️ PHISHING |

---

## 🐛 Bug Fixed

The original import statement had an error:

```python
# ❌ Wrong
import sklearn.ensemble 
import RandomForestClassifier

# ✅ Correct
from sklearn.ensemble import RandomForestClassifier
```

---

## ⚠️ Limitations

- The training dataset is very small (8 URLs) — for real-world use, thousands of samples are needed.
- Only 3 features are used — real phishing detectors use many more (HTTPS, domain age, redirects, etc.).
- This is a **learning project**, not a production security tool.

---

## 📚 Concepts Used

- `pandas` — data handling with DataFrames
- `scikit-learn` — machine learning (Random Forest)
- Feature engineering from raw strings
- Binary classification (Safe vs Phishing)

---

*© Chitrakshi Chauhan | VIT Bhopal University | 2025–26*
