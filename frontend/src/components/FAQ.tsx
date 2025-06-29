import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';

const FAQ = () => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const faqs = [
    {
      question: 'How does AEIXBT analyze sustainability?',
      answer: 'AEIXBT combines on-chain transaction data, energy consumption metrics, and governance patterns with machine learning algorithms to provide comprehensive sustainability scores. We analyze factors including carbon footprint, renewable energy usage, governance transparency, and social impact metrics.',
    },
    {
      question: 'Which tokens and blockchains are supported?',
      answer: 'We currently support major blockchains including Ethereum, Polygon, Binance Smart Chain, Solana, and Cardano. Our database covers over 10,000 tokens and is continuously expanding. We prioritize tokens with significant market cap and active governance structures.',
    },
    {
      question: 'What makes the AI-powered RAG model unique?',
      answer: 'Our Retrieval-Augmented Generation model is specifically trained on Web3 sustainability data, ESG frameworks, and blockchain governance patterns. It can correlate complex sustainability metrics with real-time blockchain activity to provide actionable insights and predictions.',
    },
    {
      question: 'How accurate are the sustainability scores?',
      answer: 'Our scoring system achieves 85-90% accuracy by combining multiple data sources including energy consumption APIs, carbon offset registries, governance voting records, and community sentiment analysis. Scores are updated in real-time and validated through cross-referencing multiple data points.',
    },
    {
      question: 'Can I integrate AEIXBT data into my application?',
      answer: 'Yes! We offer comprehensive APIs for developers and enterprises. Our RESTful APIs provide sustainability scores, governance analytics, and environmental impact data. We also offer webhook integration for real-time updates and bulk data exports for research purposes.',
    },
    {
      question: 'What data sources does AEIXBT use?',
      answer: 'We aggregate data from blockchain explorers, energy consumption databases, governance platforms, carbon registries, social media sentiment, academic research, and verified sustainability reports. All data sources are vetted for accuracy and updated continuously.',
    },
  ];

  const toggleFAQ = (index: number) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <section id="faq" className="py-20 bg-gray-800/30">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">
            <span className="bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
              Frequently Asked Questions
            </span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Everything you need to know about AEIXBT and Web3 sustainability analysis.
          </p>
        </div>

        <div className="space-y-4">
          {faqs.map((faq, index) => (
            <div
              key={index}
              className="bg-gray-900/50 backdrop-blur-sm border border-gray-700 rounded-xl overflow-hidden hover:border-emerald-500/50 transition-all duration-300"
            >
              <button
                onClick={() => toggleFAQ(index)}
                className="w-full px-6 py-5 text-left flex items-center justify-between hover:bg-gray-800/50 transition-colors"
              >
                <h3 className="text-lg font-semibold text-white pr-4">
                  {faq.question}
                </h3>
                {openIndex === index ? (
                  <ChevronUp className="h-5 w-5 text-emerald-400 flex-shrink-0" />
                ) : (
                  <ChevronDown className="h-5 w-5 text-gray-400 flex-shrink-0" />
                )}
              </button>
              
              {openIndex === index && (
                <div className="px-6 pb-5">
                  <div className="border-t border-gray-700 pt-4">
                    <p className="text-gray-300 leading-relaxed">
                      {faq.answer}
                    </p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FAQ;