import { useState } from 'react';
import JournalForm from './components/JournalForm';

function App() {
  const [entries, setEntries] = useState([]);

  const handleAddEntry = (entry) => {
    // Send POST request to backend
    fetch('http://localhost:8000/entries', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: entry.title,
        body: entry.body
      })
    })
    .then(response => response.json())
    .then(data => {
      setEntries([data, ...entries]);
    })
    .catch(error => {
      console.error('Error saving entry:', error);
    });
  };

  return (
    <div className="min-h-screen bg-gray-100 text-gray-900 p-8">
      <h1 className="text-3xl font-bold mb-6">My Daily Journal</h1>
      <JournalForm onSubmit={handleAddEntry} />

      <div>
        {entries.map((entry, index) => (
          <div key={index} className="bg-white p-4 rounded shadow mb-4">
            <h3 className="text-lg font-semibold">{entry.title}</h3>
            <p className="text-sm text-gray-500">{entry.date}</p>
            <p className="mt-2">{entry.body}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
