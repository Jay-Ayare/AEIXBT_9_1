import React from 'react';
import { BarChart3, Leaf, Bot, Shield, Globe, Zap } from 'lucide-react';

const Features = () => {
  const features = [
    {
      icon: <BarChart3 className="h-12 w-12 text-emerald-400" />,
      title: 'On-chain & Off-chain Intelligence',
      description: 'Comprehensive analysis combining blockchain data with external sustainability metrics for complete insights.',
    },
    {
      icon: <Leaf className="h-12 w-12 text-emerald-400" />,
      title: 'ESG-Focused Token Insights',
      description: 'Environmental, social, and governance scoring for Web3 projects with real-time sustainability tracking.',
    },
    {
      icon: <Bot className="h-12 w-12 text-emerald-400" />,
      title: 'AI-Powered RAG Model',
      description: 'Advanced retrieval-augmented generation for intelligent analysis and predictive sustainability modeling.',
    },
    {
      icon: <Shield className="h-12 w-12 text-teal-400" />,
      title: 'Governance Analysis',
      description: 'Deep dive into DAO structures, voting patterns, and decision-making processes for transparency insights.',
    },
    {
      icon: <Globe className="h-12 w-12 text-teal-400" />,
      title: 'Carbon Footprint Tracking',
      description: 'Monitor and analyze the environmental impact of blockchain operations and token transactions.',
    },
    {
      icon: <Zap className="h-12 w-12 text-teal-400" />,
      title: 'Real-time Monitoring',
      description: 'Live tracking of sustainability metrics with instant alerts for significant changes or improvements.',
    },
  ];

  return (
    <section id="features" className="py-20 bg-gray-800/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold mb-4">
            <span className="bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
              Powerful Features
            </span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Cutting-edge tools for comprehensive Web3 sustainability analysis and intelligent decision-making.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="group bg-gray-900/50 backdrop-blur-sm border border-gray-700 rounded-2xl p-8 hover:border-emerald-500/50 transition-all duration-300 hover:shadow-lg hover:shadow-emerald-500/10 hover:-translate-y-1"
            >
              <div className="mb-6 transform group-hover:scale-110 transition-transform duration-300">
                {feature.icon}
              </div>
              <h3 className="text-xl font-semibold mb-4 text-white group-hover:text-emerald-400 transition-colors">
                {feature.title}
              </h3>
              <p className="text-gray-400 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;