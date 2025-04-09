import { useState } from 'react';

function JournalForm({ onSubmit }) {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim() && body.trim()) {
      onSubmit({ title, body });
      setTitle('');
      setBody('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded p-6 mb-6">
      <h2 className="text-xl font-semibold mb-4">New Journal Entry</h2>
      <input
        className="w-full border border-gray-300 rounded p-2 mb-4"
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        className="w-full border border-gray-300 rounded p-2 mb-4"
        placeholder="Write your thoughts here..."
        rows={5}
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Save Entry
      </button>
    </form>
  );
}

export default JournalForm;