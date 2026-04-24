import React from 'react';

const ResultDashboard = ({ result }) => {
  if (!result) {
    return (
      <div className="empty-state">
        <p>Awaiting application data...</p>
      </div>
    );
  }

  const { eligibility, probability, risk_level, explanation } = result;

  return (
    <div className="result-card">
      <h2 style={{ marginBottom: '1.5rem', fontFamily: "'Outfit', sans-serif" }}>Decision Engine</h2>
      
      <div className="prob-circle" data-risk={risk_level}>
        {(probability * 100).toFixed(1)}%
      </div>

      <div className={`result-status ${eligibility ? 'status-approved' : 'status-rejected'}`}>
        {eligibility ? 'APPROVED' : 'REJECTED'}
      </div>

      <p style={{ fontSize: '1.1rem', color: 'var(--text-muted)', marginBottom: '2rem' }}>
        Assessed Risk Level: <span style={{ fontWeight: 'bold' , color: risk_level === 'Low' ? 'var(--success)' : (risk_level === 'High' ? 'var(--danger)' : 'var(--warning)') }}>{risk_level}</span>
      </p>

      <h3 style={{ textAlign: 'left', marginBottom: '1rem', borderBottom: '1px solid var(--panel-border)', paddingBottom: '0.5rem' }}>
        Top Factors (Explainability)
      </h3>
      
      <ul className="explanation-list">
        {Object.entries(explanation).map(([feature, impact], idx) => (
          <li key={idx} className="explanation-item">
            <span style={{ textTransform: 'capitalize' }}>
              {feature.replace(/_/g, ' ')}
            </span>
            <span className={`badge ${impact > 0 ? 'badge-success' : 'badge-danger'}`}>
              {impact > 0 ? '+' : ''}{impact.toFixed(3)}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ResultDashboard;
