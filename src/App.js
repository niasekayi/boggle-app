import React, { useState, useEffect } from "react";
import "./App.css";

const INITIAL_GRID = [
  ["T", "W", "Y", "R"],
  ["E", "N", "P", "H"],
  ["G", "St", "Qu", "R"],
  ["O", "N", "T", "A"],
];

const DICTIONARY = [
  "art", "ego", "gent", "get", "net", "new", "newt",
  "prat", "pry", "qua", "quart", "quartz", "rat",
  "tar", "tarp", "ten", "went", "wet", "arty", "not"
];

function App() {
  const [started, setStarted] = useState(false);
  const [timeLeft, setTimeLeft] = useState(180); // 3 minutes
  const [wordInput, setWordInput] = useState("");
  const [foundWords, setFoundWords] = useState([]);
  const [message, setMessage] = useState("");

  // timer
  useEffect(() => {
    if (!started) return;
    if (timeLeft === 0) {
      handleStop();
      return;
    }
    const timer = setInterval(() => setTimeLeft((t) => t - 1), 1000);
    return () => clearInterval(timer);
  }, [started, timeLeft]);

  const handleStart = () => {
    setStarted(true);
    setTimeLeft(180);
    setFoundWords([]);
    setMessage("");
  };

  const handleStop = () => {
    setStarted(false);
    setMessage("Time’s up! 💗 Here were your words!");
  };

  const handleSubmitWord = () => {
    const word = wordInput.toLowerCase().trim();
    setWordInput("");

    if (!started) {
      setMessage("Click start to play!");
      return;
    }

    if (foundWords.includes(word)) {
      setMessage(`You already found “${word.toUpperCase()}”! 😅`);
      return;
    }

    if (DICTIONARY.includes(word)) {
      setFoundWords([...foundWords, word]);
      setMessage(`Nice! “${word.toUpperCase()}” is valid 💕`);
    } else {
      setMessage(`“${word.toUpperCase()}” isn’t valid 💭`);
    }
  };

  const formatTime = (sec) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m}:${s.toString().padStart(2, "0")}`;
  };

  return (
    <div className="App">
      <h1 className="title">💖 Boggle Bliss 💖</h1>

      <div className="controls">
        {!started && (
          <button className="start-btn" onClick={handleStart}>
            Start Game
          </button>
        )}
        {started && (
          <button className="stop-btn" onClick={handleStop}>
            Stop Game
          </button>
        )}
        {started && <h2 className="timer">⏰ {formatTime(timeLeft)}</h2>}
      </div>

      {started && (
        <div className="board">
          {INITIAL_GRID.map((row, i) => (
            <div key={i} className="row">
              {row.map((cell, j) => (
                <div key={j} className="tile">
                  {cell}
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {started && (
        <div className="input-area">
          <input
            type="text"
            value={wordInput}
            onChange={(e) => setWordInput(e.target.value)}
            placeholder="Type a word..."
          />
          <button onClick={handleSubmitWord}>Submit</button>
        </div>
      )}

      <p className="message">{message}</p>

      <div className="word-list">
        <h3>Words Found ({foundWords.length})</h3>
        <ul>
          {foundWords.map((w, i) => (
            <li key={i}>{w.toUpperCase()}</li>
          ))}
        </ul>
      </div>

      {!started && foundWords.length > 0 && (
        <div className="summary">
          <h3>💌 Your Found Words</h3>
          <ul>
            {foundWords.map((w, i) => (
              <li key={i}>{w.toUpperCase()}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
