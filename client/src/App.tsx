import { useState } from 'react'
// import Combobox from 'react-widgets/Combobox'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://github.com/liammccall" target="_blank">
          <img src="http://localhost:5002/image1" className="logo" alt="Map" />
        </a>
      </div>
      <h1>GiAtlas</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test hmr
        </p>
      </div>
      <p className="read-the-docs">
        GRGIS
      </p>
    </>
  )
}

export default App
