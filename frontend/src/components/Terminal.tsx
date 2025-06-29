import React, { useState } from "react";
import ReactMarkdown from "react-markdown";

const Terminal = () => {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [isTyping, setIsTyping] = useState(false);

  const handleSubmit = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setAnswer("");
    setIsTyping(false);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      setAnswer(data.response);
      setIsTyping(true);
    } catch (err) {
      setAnswer("⚠️ Failed to fetch response. Try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && e.ctrlKey) handleSubmit();
  };

  return (
    <section id="terminal" className="py-20 bg-gray-900">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">
            <span className="bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
              AI Analysis Terminal
            </span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Interact with our AI to analyze token sustainability, governance structures, and environmental impact.
          </p>
        </div>

        <div
          className="w-full max-w-4xl mx-auto p-6 bg-black/20 backdrop-blur-lg rounded-xl border border-emerald-400/30 shadow-xl"
        >
          <h3 className="text-3xl font-semibold text-center text-emerald-400 mb-4">
            Sustainability Terminal
          </h3>

          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyPress}
            placeholder="Ask about a token, DAO, or sustainability metric..."
            className="w-full h-32 p-4 rounded-lg border border-emerald-300 bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-400/40"
          />

          <div className="flex justify-between items-center mt-2 text-sm text-gray-400">
            <span>Ctrl + Enter to submit</span>
            <button
              onClick={handleSubmit}
              disabled={loading}
              className={`px-6 py-2 rounded-full font-semibold transition-all ${
                loading
                  ? "bg-gray-600 cursor-not-allowed"
                  : "bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white shadow"
              }`}
            >
              {loading ? "Analyzing..." : "🔍 Analyze"}
            </button>
          </div>

          {answer && (
            <div className="mt-6 bg-white/10 p-6 rounded-lg border border-white/20 animate-fade-in text-white">
              <ReactMarkdown className="prose prose-invert prose-lg max-w-none">
                {answer}
              </ReactMarkdown>
            </div>
          )}
        </div>
      </div>
    </section>
  );
};

export default Terminal;