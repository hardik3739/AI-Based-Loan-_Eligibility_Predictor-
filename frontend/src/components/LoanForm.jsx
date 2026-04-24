import React, { useState } from 'react';

const LoanForm = ({ onResult }) => {
  const [formData, setFormData] = useState({
    age: 30,
    income: 60000,
    employment_years: 5,
    savings_ratio: 0.2,
    expense_ratio: 0.5,
    transaction_frequency: 20,
    income_stability_score: 0.8,
    payment_consistency: 0.9
  });
  
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      onResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const fd = new FormData();
    fd.append('file', file);
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/explain', {
        method: 'POST',
        body: fd
      });
      const data = await response.json();
      if (data.results && data.results.length > 0) {
        onResult(data.results[0]); 
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2 style={{ marginBottom: '1.5rem', fontFamily: "'Outfit', sans-serif" }}>Application Details</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
          <div className="form-group">
            <label>Age</label>
            <input type="number" name="age" className="form-control" value={formData.age} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Income ($)</label>
            <input type="number" name="income" className="form-control" value={formData.income} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Employment (Years)</label>
            <input type="number" name="employment_years" className="form-control" value={formData.employment_years} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Savings Ratio</label>
            <input type="number" step="0.01" name="savings_ratio" className="form-control" value={formData.savings_ratio} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Expense Ratio</label>
            <input type="number" step="0.01" name="expense_ratio" className="form-control" value={formData.expense_ratio} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Txn Frequency / mo</label>
            <input type="number" name="transaction_frequency" className="form-control" value={formData.transaction_frequency} onChange={handleChange} required />
          </div>
        </div>
        <button type="submit" className="btn btn-primary" disabled={loading}>
          {loading ? 'Analyzing...' : 'Predict Eligibility'}
        </button>
      </form>

      <div style={{ margin: '2rem 0', textAlign: 'center', color: 'var(--text-muted)' }}>
        <span style={{ display: 'inline-block', width: '40%', height: '1px', background: 'var(--panel-border)', verticalAlign: 'middle' }}></span>
        <span style={{ padding: '0 1rem' }}>OR</span>
        <span style={{ display: 'inline-block', width: '40%', height: '1px', background: 'var(--panel-border)', verticalAlign: 'middle' }}></span>
      </div>

      <div className="file-upload-wrapper" onClick={() => document.getElementById('csvUpload').click()}>
        <input id="csvUpload" type="file" accept=".csv" style={{ display: 'none' }} onChange={handleFileUpload} />
        <p style={{ fontWeight: 600, color: 'var(--text-main)' }}>Upload Transaction CSV</p>
        <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginTop: '0.5rem' }}>Extract patterns automatically</p>
      </div>
    </div>
  );
};

export default LoanForm;
