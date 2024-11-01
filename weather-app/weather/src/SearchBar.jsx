import {useState} from 'react'
import { Button, Form } from 'react-bootstrap'


// Creating SearchBar component and passing in the value returned by getWeatherData
const SearchBar = ({getWeatherData}) => {
    // Using a hook that takes in the userInput and creating a setUserInput function
    // And setting the default state of the userInput to an empty string using the useState() function.
    const [userInput, setUserInput] = useState("")
    
    // Creating a handleSubmit function that takes in the event
    const handleSubmit = (event) => {
        event.preventDefault()
        console.log(userInput)
        getWeatherData(userInput)
        setUserInput("")
    }
    return (
    <div>
        <Form onSubmit={handleSubmit} className="flex justify-center mb-4">
            <Form.Control
                type='search'
                placeholder='Enter Location'
                onChange={(event) => setUserInput(event.target.value)}
                value={userInput}/>
            <Button type='Submit'>Search</Button>
        </Form>
    </div>
    )
}

export default SearchBar