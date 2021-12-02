import './App.css';
import React from 'react'
import { Link } from 'react-router-dom'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          K-AI Dungeon
        </p>
        <nav>
          <Link to="/dialogue">
            <button>Click to Start</button>
          </Link>
        </nav>

      </header>

    </div>
  );
}

export default App;
