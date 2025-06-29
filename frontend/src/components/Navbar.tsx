import React, { useState, useEffect } from 'react';
import { Menu, X, Terminal as TerminalIcon } from 'lucide-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
    setIsOpen(false);
  };

  return (
    <nav className={`fixed top-0 w-full z-50 transition-all duration-300 ${
      scrolled ? 'bg-gray-900/95 backdrop-blur-md border-b border-gray-800' : 'bg-transparent'
    }`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center space-x-2">
            <TerminalIcon className="h-8 w-8 text-emerald-400" />
            <span className="text-xl font-bold bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">
              AEIXBT
            </span>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <button onClick={() => scrollToSection('home')} className="hover:text-emerald-400 transition-colors">
              Home
            </button>
            <button onClick={() => scrollToSection('features')} className="hover:text-emerald-400 transition-colors">
              Features
            </button>
            <button onClick={() => scrollToSection('faq')} className="hover:text-emerald-400 transition-colors">
              FAQ
            </button>
            <button onClick={() => scrollToSection('contact')} className="hover:text-emerald-400 transition-colors">
              Contact
            </button>
            <button
              onClick={() => scrollToSection('terminal')}
              className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-6 py-2 rounded-full hover:from-emerald-600 hover:to-teal-600 transition-all duration-300 shadow-lg hover:shadow-emerald-500/25"
            >
              Launch Terminal
            </button>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-gray-300 hover:text-white"
            >
              {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden bg-gray-900/95 backdrop-blur-md border-t border-gray-800">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <button onClick={() => scrollToSection('home')} className="block px-3 py-2 text-gray-300 hover:text-emerald-400 transition-colors">
                Home
              </button>
              <button onClick={() => scrollToSection('features')} className="block px-3 py-2 text-gray-300 hover:text-emerald-400 transition-colors">
                Features
              </button>
              <button onClick={() => scrollToSection('faq')} className="block px-3 py-2 text-gray-300 hover:text-emerald-400 transition-colors">
                FAQ
              </button>
              <button onClick={() => scrollToSection('contact')} className="block px-3 py-2 text-gray-300 hover:text-emerald-400 transition-colors">
                Contact
              </button>
              <button
                onClick={() => scrollToSection('terminal')}
                className="block w-full text-left bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-3 py-2 rounded-lg hover:from-emerald-600 hover:to-teal-600 transition-all duration-300 mt-2"
              >
                Launch Terminal
              </button>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;