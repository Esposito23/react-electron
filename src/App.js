import React, { Component } from 'react';
import './App.css';
import Rotante from './moduli/rotante/Rotante' 
import Lineare from './moduli/Lineare/Lineare'
import Xbee from './moduli/XbeeUsb/Xbee'
import Pressione from './moduli/Pressione/Pressione'
import Lpump from './moduli/Lpump/Lpump'
import Valvole from './moduli/Valvole/Valvole'


export default class App extends Component {
  render() {
    return (
      <div className='App-header'>
        <Rotante />
        <Lineare />
        <Xbee />
        <Pressione />
        <Lpump />
        <Valvole />
      </div>

    )
  }
}

