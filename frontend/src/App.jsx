import React, { useState, useEffect } from 'react';
import LoanForm from './components/LoanForm';
import ResultDashboard from './components/ResultDashboard';
import FairnessReport from './components/FairnessReport';

function App() {
  const [result, setResult] = useState(null);
  const [fairnessData, setFairnessData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/fairness')
      .then(res => res.json())
      .then(data => {
        if (!data.error) setFairnessData(data);
      })
      .catch(err => console.error("Could not fetch fairness report", err));
  }, []);

  return (
    <div className="app-container">
      <header className="header">
        <h1>AI Loan Predictor</h1>
        <p>Fair, Explainable, & Data-Driven Financial Inclusion</p>
      </header>

      <main className="grid-layout">
        <div className="glass-panel">
          <LoanForm onResult={setResult} />
        </div>
        
        <div className="glass-panel" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <ResultDashboard result={result} />
        </div>
      </main>

      {fairnessData && (
        <div className="glass-panel" style={{ marginTop: '2rem' }}>
          <FairnessReport data={fairnessData} />
        </div>
      )}
    </div>
  );
}

export default App;
