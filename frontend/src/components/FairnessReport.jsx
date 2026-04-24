import React from 'react';

const FairnessReport = ({ data }) => {
  const { approval_rates_by_income, mitigation_suggestion } = data;

  return (
    <div>
      <h2 style={{ marginBottom: '1.5rem', fontFamily: "'Outfit', sans-serif" }}>Bias & Fairness Monitor</h2>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        <div>
          <h3 style={{ marginBottom: '1rem', fontSize: '1.1rem', color: 'var(--text-muted)' }}>Approval Rates by Income Group</h3>
          {Object.entries(approval_rates_by_income).map(([group, rate]) => (
            <div key={group} className="fairness-stat">
              <div className="fairness-header">
                <span>{group} Income</span>
                <span>{(rate * 100).toFixed(1)}%</span>
              </div>
              <div className="fairness-bar-bg">
                <div className="fairness-bar-fill" style={{ width: `${rate * 100}%` }}></div>
              </div>
            </div>
          ))}
        </div>
        
        <div style={{ background: 'rgba(15, 23, 42, 0.4)', borderRadius: '12px', padding: '1.5rem', border: '1px solid var(--panel-border)' }}>
          <h3 style={{ marginBottom: '1rem', fontSize: '1.1rem', color: 'var(--text-muted)' }}>Automated System Suggestions</h3>
          <p style={{ color: 'var(--warning)', lineHeight: '1.6' }}>
            {mitigation_suggestion}
          </p>
        </div>
      </div>
    </div>
  );
};

export default FairnessReport;
