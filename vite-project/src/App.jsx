import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'

import Home from './pages/Home'
import LineChartPage from './pages/LineChartPage'

import './App.css'

function App() {
  const navigationActive = (({isActive}) => {
    return {
      color: isActive? 'grey' : 'black',
      textDecoration: 'none'
    }
  })
  return (
    <Router>
      <nav>
        <NavLink style={navigationActive} to='home'>
          Home
        </NavLink>
        <NavLink style={navigationActive} to='temperatures'>
          Temperatures
        </NavLink>
        <NavLink style={navigationActive} to='base-temperatures'>
          Base Temperatures
        </NavLink>
      </nav>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/temperatures' element={<LineChartPage />} />
      </Routes>
    </Router>


  )
}

export default App
