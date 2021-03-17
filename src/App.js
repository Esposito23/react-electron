import React, { Component } from 'react';
import './App.css';

export default class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      msg: 'Clicca per il comando'
    }
  }
  ComandoOn = () => {
    fetch('/motorOn')
      .then(res => res.json())
      .then(mess => {
        this.setState({ msg: mess.m });
      })
  }
  ComandoOff = () => {
    fetch('/motorOff')
      .then(res => res.json())
      .then(mess => {
        this.setState({ msg: mess.m });
      })
  }

  render() {
    return (
      <div className='App-header'>
        <p>{this.state.msg}</p>
        <button onClick={this.ComandoOn}>Accendi !</button>
        <button onClick={this.ComandoOff}>Spegni !</button>
      </div>
    )
  }
}




// imp