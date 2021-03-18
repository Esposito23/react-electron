import React, { Component } from 'react';
import './App.css';
import Rotante from './moduli/rotante/Rotante' 
import Lineare from './moduli/Lineare/Lineare'


export default class App extends Component {
  render() {
    return (
      <div className='App-header'>
        <Rotante />
        <Lineare />
      </div>

    )
  }
}

