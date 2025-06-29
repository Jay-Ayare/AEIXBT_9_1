import React, { useState } from "react";
import ReactMarkdown from 'react-markdown';
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setAnswer("Thinking...");

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ query }),
});


      const data = await response.json();
      setAnswer(data.response);  // ✅ Fixed key
    } catch (err) {
      setAnswer("⚠️ Failed to get a response. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div className="app-container p-4 min-h-screen text-white">
      <h1 className="neon-text mb-4">AEIXBT | Sustainability Chat</h1>

      <textarea
        className="custom-input w-full p-2 mb-4 rounded"
        rows="4"
        placeholder="Ask a sustainability-related question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button
        className="btn-emerald px-4 py-2 rounded mb-6"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Submit"}
      </button>

      {answer && (
        <div className="response-box p-4">
          <ReactMarkdown>{answer}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;
