import React from 'react';
import './goddess.css';

const FloatingGoddess = () => (
  <div className="goddess-container">
    <img 
      src="/assets/goddess.png" 
      alt="Wisdom Goddess" 
      className="floating-goddess"
    />
    <div className="aura-effect"></div>
  </div>
);

export default FloatingGoddess;