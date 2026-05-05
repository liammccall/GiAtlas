import React, { useState, useEffect, useRef } from 'react'
// import Combobox from 'react-widgets/Combobox'
import './App.css'

function App() {
  const [file_name, setFile_name] = useState<string>("coastline")

  const inputField = useRef<HTMLInputElement>(null);

  useEffect(() => {
    fetch('/api/save_image',{
      method: "PUT",
      body: JSON.stringify({data:file_name})
    }).then()

  }, [file_name])

  return (
    <>
      <div>
        <a href="https://github.com/liammccall" target="_blank">
          <img src="http://localhost:5002/image1" className="logo" alt="Map" />
        </a>
      </div>
      <div>
        <a href="https://github.com/liammccall" target="_blank">
          <img src="http://localhost:5002/image2" className="logo" alt="Map" />
        </a>
      </div>
      <h1>GiAtlas</h1>
      <div className="card">
        <input type="text" ref={inputField}/>
        <button onClick={() => setFile_name(inputField.current?.value ?? "")}>
          Fetch
        </button>
      </div>
      <p className="read-the-docs">
        GRGIS
      </p>
    </>
  )
}

export default App
