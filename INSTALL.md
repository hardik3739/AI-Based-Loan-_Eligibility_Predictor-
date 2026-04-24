# Installation Guide

Follow these steps to run the AI-Based Loan Eligibility Predictor locally.

## Prerequisites

- Node.js (v16+)
- Python (3.9+)

## 1. Backend Setup

Open a terminal and navigate to the project root:

```bash
cd AI-Loan-Predictor

# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate Synthetic Data
# This will create data/sample_transactions.csv
python data/generate_dataset.py

# 5. Start the FastAPI Server
# The startup event will automatically train the initial model if not found.
cd backend
uvicorn main:app --reload --port 8000
```
*The API will be available at `http://localhost:8000/docs` (Swagger UI).*

## 2. Frontend Setup

Open a separate terminal window:

```bash
cd AI-Loan-Predictor/frontend

# 1. Install dependencies
npm install

# 2. Start the development server
npm run dev
```

*The frontend will typically run at `http://localhost:5173`. Open this URL in your browser to view the application.*
