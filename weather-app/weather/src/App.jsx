// Necessary imports
import axios from 'axios';
import './App.css'
import SearchBar from './SearchBar';


function App() {

  // Initializing apikey variable and setting it to the value of the API Key as a string for validation
  const apikey = "b354dc157fe94899af3195009243110"

  // useEffect( () => {
  //   console.log(userInput);
  // }, [userInput]
  // )

  // Creating getWeatherData component as async function that takes in what user types 
  const getWeatherData = async (userInput) => {
    console.log("GetWeatherData Input: " + userInput)

    // Creating response variable that is equal to the data that is grabbed from the API using the API Key and reading the user input
    const response = await axios.get(`http://api.weatherapi.com/v1/current.json?key=${apikey}&q=${userInput}`)
    console.log(response)
  }

  // Returning the SearchBar component and runnning getWeatherData function with SearchBar component.
  return (
    <>
      <SearchBar getWeatherData={getWeatherData}/>
    </>
  )
}

export default App