


import { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult('');
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult('');
    setError('');
    if (!file) {
      setError('Please select a PDF file.');
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const response = await fetch('http://127.0.0.1:8000/predict_pdf/', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
      } else {
        setError(data.error || 'Prediction failed.');
      }
    } catch (err) {
      setError('Server error. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="center-bg">
      <div className="center-card">
        <div className="center-icon" aria-label="pdf icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1a4fa0" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="18" height="18" rx="6" fill="#eaf6ff"/><path d="M7 7h10v10H7z" fill="#fff"/><path d="M9 13h6M9 9h6" stroke="#1a4fa0"/><path d="M9 17h2" stroke="#1a4fa0"/></svg>
        </div>
        <h1>Email PDF Spam Classifier</h1>
        <p className="subtitle">Upload a PDF email to check if it is <b>SPAM</b> or <b>Non-SPAM</b></p>
        <form onSubmit={handleSubmit}>
          <input
            type="file"
            accept="application/pdf"
            onChange={handleFileChange}
            className="file-input"
          />
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? 'Analyzing...' : 'Classify PDF'}
          </button>
        </form>
        {result && (
          <div className={`result ${result === 'SPAM' ? 'spam' : 'ham'}`}>{result}</div>
        )}
        {error && <div className="error">{error}</div>}
        <footer className="footer">Made with <span role="img" aria-label="love">💙</span> for CyberML Project</footer>
      </div>
    </div>
  );
}

export default App;
