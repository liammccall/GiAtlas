import { useState, useRef, useCallback } from 'react'
import './App.css'

import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

function App() {
  const webserverUrl = "http://localhost:5002"

  // const [fileName, setFileName] = useState("coastline")
  // const [query, setQuery] = useState("")
  const [geoKey, _coreSetGeoKey] = useState(0)
  const [geoData, _coreSetGeoData] = useState<GeoJSON.GeoJsonObject>()

  const inputField = useRef<HTMLInputElement>(null)
  const natEarthField = useRef<HTMLInputElement>(null)

  // useEffect(() => {
  //   (async () => {
  //     await fetch(webserverUrl + '/api/save_image',{
  //       method: "POST",
  //       headers: {'Content-Type': 'application/json'},
  //       body: JSON.stringify({file_name:fileName})
  //     })

  //     console.log("saved" + fileName)

  //     const response = await fetch(
  //       `${webserverUrl}/geojson/${fileName}?t=${Date.now()}`
  //     )

  //     console.log("fetched" + fileName)

  //     const data = await response.json()

  //     setGeoData(data)

  //     console.log("set" + fileName)
  //   })()
  // }, [fileName])


  
  
  const generateMap = useCallback(async (query: string) => {

      const response = await fetch(webserverUrl + '/api/query',{
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({file_name:query})
      })

      function setGeoData(data: GeoJSON.GeoJsonObject) {
        _coreSetGeoKey(k => k + 1)
        _coreSetGeoData(data)
      }

      console.log("fetched: " + query)

      const data = await response.json()

      setGeoData(data)

      console.log("set: " + query)
    }
  , [webserverUrl])

  function saveNatEarth(fileName: string): void{
      (async () => {
        await fetch(webserverUrl + '/api/save_image',
          {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({file_name:fileName})
          });
      })();
  }

  return (
    <>
      <h1>GiAtlas</h1>

      <div className="card">
        <input type="text" ref={inputField} />

        <button
          onClick={() =>
            generateMap(inputField.current?.value ?? "")
          }
        >
          Query
        </button>
      </div>

      <div className="card">
        <input type="text" ref={natEarthField} />

        <button
          onClick={() =>
            saveNatEarth(natEarthField.current?.value ?? "")
          }
        >
          Save
        </button>
      </div>

      <MapContainer
        center={[20, 0]}
        zoom={2}
        style={{
          height: "600px",
          width: "100%"
        }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {geoData && <GeoJSON data={geoData} key={geoKey}/>}
      </MapContainer>
    </>
  )
}

export default App