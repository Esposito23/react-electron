import React, { Component } from 'react';
import '../../App.css'

class Valvole extends Component {

  constructor(props) {
    super(props)
    this.state = {
      state: 'Clicca per lo stato Valvole',
      l1 : 'Clicca per cambiare l1'
    }
  }
  ValvL1 = () => {
    fetch('/valvGet')
      .then(res => res.json())
      .then(mess => {
        this.setState({ l1: mess.state });
      })
  }

  ValvState = () => {
    fetch('/valvState')
      .then(res => res.json())
      .then(mess => {
        this.setState({ state: mess.state });
      })
  }
  ValvChange = () => {
    fetch('/valvSet')
      .then(res => res.json())
      .then(mess => {
        this.setState({ l1: mess.state });
      })
  }
  render() {
    return (
      <div className='App-header'>
        <h1>Valvole Fluidica</h1>
        <p>{this.state.state}</p>
        <button onClick={this.ValvState}>Stato del sistema</button>
        <p>{this.state.l1}</p>
        <button onClick={this.ValvL1}>Chiedi stato L1</button>
        <button onClick={this.ValvChange}>Cambia stato L1</button>
      </div>

    )
  }
}

export default Valvole;
