import {useState} from 'react'
import { Button, Form } from 'react-bootstrap'



const SearchBar = ({getWeatherData}) => {
    const [userInput, setUserInput] = useState("")
    
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