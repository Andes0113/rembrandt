import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'
import logo from './assets/logo.png'

async function generateImage(urls, prompt) {
  const response = await axios.post('http://3.15.178.30:8000/generate', {
    urls,
    prompt,
  });
  return response.data;
}

// function Input({ value, setValue }) {
//   return (
//   );
// }

function App() {
  const [inputUrls, setInputUrls] = useState([
    ''
  ]);
  const [prompt, setPrompt] = useState('');
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);

  console.log(inputUrls);


  async function getImage() {
    setLoading(true);
    try {
      const urls = inputUrls.slice(0, -1);
      if (urls.length > 0 && prompt != '') {
        const output = await generateImage(urls, prompt);
        if (output.success) setUrl(output.url);  
      } else {
        setError(true);
      }
    } catch(err) {
      console.log(err);
      setError(true);
    } finally {
      setLoading(false);
    }
  }

  function setInputUrl(url, idx) {
    inputUrls[idx] = url;
    setInputUrls([...inputUrls])
  }

  function addNewUrl() {
    if (inputUrls[inputUrls.length - 1] !== '') {
      setInputUrls([...inputUrls, ''])
    }
  }

  return (
    <div id="container">

      <div id = "content">

        <div id = "header">
          <img src={logo} height="100rem"/>
        </div>

        <div id="inputs">
          <div id='imgCarousel' className={inputUrls.slice(0, -1).length == 0 ? 'hidden' : ''}>
            {inputUrls.slice(0, -1).map((url, idx) => (
              <img
                className="carouselImg"
                onError={() => setInputUrls([...inputUrls.slice(0, idx), ...inputUrls.slice(idx + 1)])}
                src={url}
                key={idx} />
            ))}
          </div>
          <div id = "inputUrl">
            <label htmlFor="inputUrl">URL:  </label>
              <input
                name="query"
                value={inputUrls[inputUrls.length - 1]}
                onChange={(e) => setInputUrl(e.target.value, inputUrls.length - 1)}
              />
            <button onClick={addNewUrl}>
              Add New Image
            </button>
          </div>

          <div id = "prompt">
            <label htmlFor="prompt">Prompt:  </label>
            <textarea name="query" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
          </div>

          <button disabled={loading} onClick={() => getImage()}>
            Generate
          </button>
        </div>
      </div>

      <div id="output">
        {url != '' && !loading &&
          <img id="image" src={url} />
        }
        {loading && 
          <img src={"https://media.discordapp.net/attachments/1210798619045793854/1211206649424117770/output-onlinegiftools.gif?ex=65ed5b18&is=65dae618&hm=c115994e497c9e49f90fd7e23f0e2b295e3223c12b42f84a9140251cd0466489&=&width=1152&height=864"}/>
        }

      </div>
    </div>
  )
}

export default App
