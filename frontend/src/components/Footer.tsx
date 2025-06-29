import React from 'react';
import { Github, BookOpen, Heart, Mail, Twitter, Linkedin } from 'lucide-react';

const Footer = () => {
  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <footer id="contact" className="bg-gray-900 border-t border-gray-800 py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
          {/* Brand Section */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <div className="h-8 w-8 bg-gradient-to-r from-emerald-400 to-teal-400 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">AX</span>
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
                AEIXBT
              </span>
            </div>
            <p className="text-gray-400 leading-relaxed max-w-md mb-6">
              Leading the future of Web3 sustainability analysis with AI-powered intelligence. 
              Making blockchain more transparent, accountable, and environmentally conscious.
            </p>
            <div className="flex space-x-4">
              <a
                href="#"
                className="bg-gray-800 hover:bg-emerald-600 text-gray-400 hover:text-white p-3 rounded-lg transition-all duration-300"
              >
                <Github className="h-5 w-5" />
              </a>
              <a
                href="#"
                className="bg-gray-800 hover:bg-emerald-600 text-gray-400 hover:text-white p-3 rounded-lg transition-all duration-300"
              >
                <Twitter className="h-5 w-5" />
              </a>
              <a
                href="#"
                className="bg-gray-800 hover:bg-emerald-600 text-gray-400 hover:text-white p-3 rounded-lg transition-all duration-300"
              >
                <Linkedin className="h-5 w-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Quick Links</h3>
            <div className="space-y-3">
              <button
                onClick={() => scrollToSection('home')}
                className="block text-gray-400 hover:text-emerald-400 transition-colors"
              >
                Home
              </button>
              <button
                onClick={() => scrollToSection('features')}
                className="block text-gray-400 hover:text-emerald-400 transition-colors"
              >
                Features
              </button>
              <button
                onClick={() => scrollToSection('terminal')}
                className="block text-gray-400 hover:text-emerald-400 transition-colors"
              >
                Terminal
              </button>
              <button
                onClick={() => scrollToSection('faq')}
                className="block text-gray-400 hover:text-emerald-400 transition-colors"
              >
                FAQ
              </button>
            </div>
          </div>

          {/* Resources */}
          <div>
            <h3 className="text-white font-semibold mb-4">Resources</h3>
            <div className="space-y-3">
              <a
                href="#"
                className="flex items-center space-x-2 text-gray-400 hover:text-emerald-400 transition-colors"
              >
                <Github className="h-4 w-4" />
                <span>GitHub</span>
              </a>
              <a
                href="#"
                className="flex items-center space-x-2 text-gray-400 hover:text-emerald-400 transition-colors"
              >
                <BookOpen className="h-4 w-4" />
                <span>Documentation</span>
              </a>
              <a
                href="#"
                className="flex items-center space-x-2 text-gray-400 hover:text-emerald-400 transition-colors"
              >
                <Mail className="h-4 w-4" />
                <span>Contact</span>
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="border-t border-gray-800 pt-8 flex flex-col sm:flex-row items-center justify-between">
          <div className="flex items-center space-x-2 text-gray-400 mb-4 sm:mb-0">
            <span>Built with</span>
            <Heart className="h-4 w-4 text-red-500" />
            <span>by Web3 researchers</span>
          </div>
          <div className="text-gray-400 text-sm">
            © 2024 AEIXBT. All rights reserved.
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;