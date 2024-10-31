import axios from 'axios';
import './App.css'


import SearchBar from './SearchBar';


function App() {

  const apikey = "b354dc157fe94899af3195009243110"

  // useEffect( () => {
  //   console.log(userInput);
  // }, [userInput]
  // )

  const getWeatherData = async (userInput) => {
    console.log("GetWeatherData Input: " + userInput)
    const response = await axios.get(`http://api.weatherapi.com/v1/current.json?key=${apikey}&q=${userInput}`)
    console.log(response)
  }

  return (
    <>
      <SearchBar getWeatherData={getWeatherData}/>
    </>
  )
}

export default App