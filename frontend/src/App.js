import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setResponse('');

    try {
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResponse(data.answer || 'No response.');
    } catch (error) {
      console.error(error);
      setResponse('⚠️ Error reaching backend.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container d-flex flex-column align-items-center justify-content-center min-vh-100 text-white">
      <h1 className="mb-4 neon-text">AEIXBT Terminal</h1>
      <form onSubmit={handleSubmit} className="w-75">
        <div className="mb-3">
          <textarea
            className="form-control custom-input"
            rows="4"
            placeholder="Ask something about the token's sustainability..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <div className="text-end">
          <button
            type="submit"
            className="btn btn-teal px-4"
            disabled={loading}
          >
            {loading ? 'Thinking...' : 'Ask'}
          </button>
        </div>
      </form>

      {response && (
        <div className="response-box mt-4 p-3 w-75">
          <h5 className="text-teal">Response:</h5>
          <p className="mb-0">{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;

