import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'

import LineChartPage from './pages/LineChartPage'

import './App.css'

function App() {
  const navigationActive = (({isActive}) => {
    return {
      color: isActive? 'grey' : 'black',
      textDecoration: 'none',
      float: 'left',
      display: 'block',
      textAlign: 'center',
      padding: '1em 2em',
      fontSize: '1.5em'
    }
  })
  return (
    <Router>
      <nav>
        <NavLink style={navigationActive} to='temperatures'>
          Temperatures
        </NavLink>
        <NavLink style={navigationActive} to='base-temperatures'>
          Base Temperatures
        </NavLink>
      </nav>
      <Routes>
        <Route path='/temperatures' element={<LineChartPage />} />
      </Routes>
    </Router>


  )
}

export default App
