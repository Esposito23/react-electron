import React, { Component } from 'react';
import '../../App.css'

class Lpump extends Component {

  constructor(props) {
    super(props)
    this.state = {
      state: 'Clicca per gestire Lpump'
    }
  }
  LPumpOff = () => {
    fetch('/lPumpOff')
      .then(res => res.json())
      .then(mess => {
        this.setState({ state: mess.state });
      })
  }
  LPumpOn = () => {
    fetch('/lPumpOn')
      .then(res => res.json())
      .then(mess => {
        this.setState({ state: mess.state });
      })
  }
  LPumpSec = () => {
    fetch('/lPumpSec')
      .then(res => res.json())
      .then(mess => {
        this.setState({ state: mess.state });
      })
  }

  render() {
    return (
      <div className='App-header'>
        <h1>Modulo Di Lpump</h1>
        <p>{this.state.state}</p>
        <button onClick={this.LPumpOff}>Attiva Lpump</button>
        <button onClick={this.LPumpOn}>Disattiva Lpump</button>
        <button onClick={this.LPumpSec}>Eroga 20ml</button>
      </div>

    )
  }
}

export default Lpump;