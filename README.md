# ⚖️ FairLens AI – Unbiased AI Decision System

## 🚀 Overview

FairLens AI is a complete **AI Bias Detection & Mitigation Platform** that helps identify, analyze, and fix bias in machine learning systems before deployment.

It ensures that AI systems used in **hiring, finance, and healthcare** are **fair, transparent, and ethical**.

---

## ❗ Problem Statement

Modern AI systems are used in high-impact decisions such as:

* Hiring candidates 👩‍💼
* Loan approvals 🏦
* Medical diagnosis 🏥

However, these systems often:

* Learn from **biased historical datasets**
* Reinforce discrimination based on **gender, race, age**
* Lack transparency in decision-making

⚠️ This leads to:

* Unfair outcomes
* Ethical concerns
* Loss of trust in AI

---

## 💡 Solution

FairLens AI provides an **end-to-end fairness pipeline** that:

1. Detects bias in datasets and models
2. Analyzes fairness using multiple metrics
3. Simulates model behavior 
4. Ai-powered Explanation using Gemini API
5. Automatically reduces bias using mitigation techniques

---

## 🔥 Key Features

### 📂 1. Dataset Upload

* Upload datasets in **CSV / JSON / Excel**
* Automatically detects:

  * Columns
  * Sensitive attributes (gender, race, etc.)

---

### 🌐 2. Multi-Domain Analysis

Supports domain-specific bias detection:

* 👩‍💼 **Hiring / Recruitment**
* 🏦 **Loan Approval**
* 🏥 **Healthcare / Medical**

Each domain focuses on relevant bias factors:

* Hiring → gender, race, education
* Loan → income, ZIP code, credit
* Healthcare → age, gender, insurance

---

### 📊 3. Bias Detection & Analysis

* Calculates fairness metrics:

  * Disparate Impact
  * Demographic Parity
  * Equal Opportunity
  * Calibration Score
* Shows **feature-level bias insights**
* Identifies **high-risk sensitive attributes**

---

### 🧪 4. Bias Simulation (Core Feature 🚀)

Compare model behavior:

#### ❌ Before Bias Fix

* Shows biased outcomes
* Highlights disparities between groups

#### ✅ After Bias Fix

* Improved fairness metrics
* Reduced bias

---

### 🤖 5. Auto Bias Fix (Smart Feature ⭐)

* Automatically applies mitigation techniques:

  * Reweighing
  * Equalized Odds
  * Data balancing
* Instantly improves fairness scores
* No manual tuning required

---

### 💡 6. AI Bias Explanation

* Uses Gemini API to:

  * Explain detected bias
  * Suggest improvements
  * Provide ethical insights

---

### 📄 7. Report Generation

* Generate structured AI fairness reports
* Useful for:

  * Audits
  * Compliance
  * Stakeholders

---

## 🧠 System Workflow

```
Upload Dataset → Multi-Domain Selection → Bias Analysis → 
Detect Bias → Auto Fix → Simulation → Report
```
## 🧪 Bias Metrics Explained

* **Disparate Impact** → Measures fairness across groups (<0.8 = biased)
* **Demographic Parity** → Equal outcomes across groups
* **Equal Opportunity** → Equal success rate
* **Predictive Parity** → Consistent predictions
* **Calibration** → Model reliability across groups

---

## 🏗️ Tech Stack

### Frontend

* HTML, CSS, JavaScript,React
* Interactive dashboard UI

### Backend

* FastAPI (Python)
* REST APIs

### AI 

* Bias detection logic
* Fairness metric computation
* Simulation engine

### Tools

* Git & GitHub
* VS Code

---

## 📁 Project Structure

```
fairlens-ai/
│
├── frontend/
│   ├── index.html
│   ├── Multi-Domain.html
│   ├── analysis.html
│   ├── simulation.html
│   ├── bias-explanation.html
│
├── backend/
│   ├── main.py
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/fairlens-ai.git
cd fairlens-ai
```

---

### 🔹 2. Backend Setup

```
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

---

### 🔹 3. Frontend Setup

* pip install uvicorn
* npm run dev
  OR
* Use VS Code Live Server

---

## 🔗 API Endpoints

### Upload Dataset

```
POST /upload
```

### Get Analysis

```
GET /analysis
```

---

## 🎯 Use Cases

* 🏢 Hiring platforms
* 🏦 Banking & finance systems
* 🏥 Healthcare AI
* 🎓 Research projects

---

## 🌍 Impact

✔ Promotes ethical AI
✔ Reduces discrimination
✔ Improves trust in AI systems
✔ Supports responsible decision-making

---

## 🔮 Future Enhancements

* Real-time bias monitoring
* Advanced visualization dashboards
* ML model integrations

---

## 👨‍💻 Developed For

Hackathon – **Unbiased AI Decision Challenge**

---

## ⭐ Support

If you found this project useful, please ⭐ the repository!
