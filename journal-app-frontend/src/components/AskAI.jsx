import { useState } from 'react';

function AskAI() {
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:8000/ask-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question }), 
        });
        const data = await response.json();
        setAnswer(data.answer);
    };

    return (
        <div className="bg-white shadow-md rounded p-6 mb-6">
            <h2 className="text-xl font-semibold mb-4">Ask AI</h2>
            <form onSubmit={handleSubmit} className="mb-4"></form>
            <input
                className="w-full border border-gray-300 rounded p-2 mb-4"
                type="text"
                placeholder="Ask a question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />
            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-red-700"
                >Ask Question</button>
            {answer && (
                <div className="mt-4">
                    <h3 className="text-lg font-semibold mb-2">AI Answer:</h3>
                    <p className="text-gray-700">{answer}</p>
                </div>
            )}
        </div>
    );
}

export default AskAI;