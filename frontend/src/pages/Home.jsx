import { useEffect, useState } from 'react';

const API_URL = import.meta.env.VITE_AI_SERVICE_URL || 'http://localhost:5000';

function Home() {
  const [response, setResponse] = useState('');

  useEffect(() => {
    fetch(`${API_URL}/api/ai/prompt`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: 'Hello from React frontend' }),
    })
      .then((res) => res.json())
      .then((data) => setResponse(data.response))
      .catch(() => setResponse('AI service not available'));
  }, []);

  return (
    <main>
      <h2>AI Service Status</h2>
      <p>{response || 'Loading...'}</p>
    </main>
  );
}

export default Home;
