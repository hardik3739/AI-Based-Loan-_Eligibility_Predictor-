# AI-Based Loan Eligibility Predictor 🚀

An end-to-end Machine Learning system that predicts loan eligibility using traditional and alternative financial data. Built with a focus on financial inclusion, fairness, and explainability.

## 🎯 Overview

This project provides a deployable, robust REST API (FastAPI) and a modern, high-performance web dashboard (React + Vite) for assessing loan applications. It goes beyond simple traditional data by incorporating alternative financial features (savings ratio, transaction frequency, consistency) to serve underbanked populations.

**[Placeholder: Live Demo Link]**

## ✨ Features

- **Advanced ML Models:** Utilizes Random Forest for robust, non-linear predictions, with Logistic Regression available as a baseline.
- **Explainability (SHAP):** Transparent AI. The system explicitly outputs the *Top 3 Factors* influencing every single decision, building trust and regulatory compliance.
- **Fairness & Bias Monitor:** Continuously evaluates approval rates across different income brackets and alerts administrators to potential disparate impact.
- **Dynamic Frontend:** A stunning, glassmorphism-inspired React dashboard tailored for high-end user experience and immediate feedback.
- **Alternative Data Engine:** Analyzes engineered features rather than raw demographic biases.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Scikit-Learn, Pandas, SHAP
- **Frontend:** React, Vite, Vanilla CSS (Custom Design System)
- **Deployment Ready:** Configured for easy standalone setup or containerization.

## 🏗️ Architecture

```text
├── backend/                  # FastAPI Application
│   ├── main.py               # API endpoints (/predict, /explain, /fairness)
│   ├── model.py              # Training logic and inference wrappers
│   ├── explain.py            # SHAP explainer implementation
│   ├── fairness.py           # Bias and metric computations
│   └── ...                   
├── frontend/                 # React UI Dashboard
│   ├── src/components/       # Modular UI blocks (Form, Results, Stats)
│   └── index.css             # High-end glassmorphism styling
├── data/                     # Data Generation and Storage
└── README.md
```

## 📸 Screenshots

![Dashboard Placeholder](/path/to/placeholder.png)

## 🚦 Getting Started

Please see **[INSTALL.md](./INSTALL.md)** for detailed step-by-step instructions on running the backend server and frontend client locally.

## 📝 License
MIT
