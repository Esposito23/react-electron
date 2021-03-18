import React, { Component } from 'react';
import '../../App.css'

class Rotante extends Component {

  constructor(props) {
    super(props)
    this.state = {
      msg: 'Clicca per gestire il motore',
      speed : 'Ultima lettura di velocità : 0',
      monitor : 'Monitor Spento'
    }
  }
  ComandoOn = () => {
    fetch('/motorOn')
      .then(res => res.json())
      .then(mess => {
        this.setState({ msg: mess.stato });
      })
  }
  ComandoOff = () => {
    fetch('/motorOff')
      .then(res => res.json())
      .then(mess => {
        this.setState({ msg: mess.stato });
      })
  }

  MonitorOn = () => {
    fetch('/monitorOn')
      .then(res => res.json())
      .then(mess => {
        this.setState({ monitor: mess.monitor });
      })
  }
  MonitorOff = () => {
    fetch('/monitorOff')
      .then(res => res.json())
      .then(mess => {
        this.setState({ monitor: mess.monitor });
      })
  }
  MonitorLast = () => {
    fetch('/monitorLast')
      .then(res => res.json())
      .then(mess => {
        this.setState({ speed: mess.speed });
      })
  }
  MonitorMean = () => {
    fetch('/monitorMean')
      .then(res => res.json())
      .then(mess => {
        this.setState({speed: mess.speed });
      })
  }
  render() {
    return (
      <div className='App-header'>
        <p>{this.state.msg}</p>
        <row>
        <button onClick={this.ComandoOn}>Accendi</button>
        <button onClick={this.ComandoOff}>Spegni</button>
        </row>
        <hr />
        <row>
        <p>{this.state.monitor}</p>
        <button onClick={this.MonitorOn}>Attiva</button>
        <button onClick={this.MonitorOff}>Disattiva</button></row>
        <hr />
        <p>{this.state.speed}</p>
        <button onClick={this.MonitorLast}>Istantanea</button>
        <button onClick={this.MonitorMean}>Media</button>
      </div>

    )
  }
}

export default Rotante;