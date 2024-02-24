import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

async function generateImage(url, prompt) {
  const response = await axios.post('http://localhost:8000/generate', {
    url,
    prompt,
  });
  return response.data;
}

function Input({ value, setValue }) {
  return (
      <input name="query" value={value} onChange={(e) => setValue(e.target.value)} />
  );
}

function App() {
  const [inputUrl, setInputUrl] = useState('');
  const [prompt, setPrompt] = useState('');
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  console.log(inputUrl);


  async function getImage() {
    setLoading(true);
    try {
      const output = await generateImage(inputUrl, prompt);
      if (output.success) setUrl(output.url);
    } catch(err) {
      console.log(err);
      setError(true);
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <div>
        <Input value={inputUrl} setValue={setInputUrl} />
        <Input value={prompt} setValue={setPrompt} />
        <button disabled={loading} onClick={() => getImage()}>
          Submit
        </button>
        {url != '' &&
          <img src={url} />
        }
      </div>
    </>
  )
}

export default App
