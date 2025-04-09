import { useState } from 'react';
import JournalForm from './components/JournalForm';

function App() {
  const [entries, setEntries] = useState([]);

  const handleAddEntry = (entry) => {
    const newEntry = { ...entry, date: new Date().toLocaleString() };
    setEntries([newEntry, ...entries]);
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
