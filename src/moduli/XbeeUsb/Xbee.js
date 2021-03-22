import React, { Component } from 'react';
import '../../App.css'

class Xbee extends Component {

  constructor(props) {
    super(props)
    this.state = {
      last: 0,
      mess : 'Clicca un bottone'
    }
  }
  lastCommand = () => {
    fetch('/xbeeLast')
      .then(res => res.json())
      .then(mess => {
        this.setState({ last: mess.last });
      })
  }

  check = () => {
    fetch('/xbeeCheck').then(res => res.json()).then(mess => {
      this.setState({mess : mess.info})
    })
  }

  reset = () => {
    fetch('/xbeeReset').then(res => res.json()).then(mess => {
      this.setState({mess : mess.info})
    })
  }


  render() {
    return (
      <div className='App-header'>
        <h1>Modulo connessione Xbee</h1>
        <p>{this.state.last}</p>
        <button onClick={this.lastCommand}> Tempo </button>
        <p>{this.state.mess}</p>
        <button onClick={this.check}> Verifica Connessione</button>
        <button onClick={this.reset}> Reset Xbee </button>
        <p>Mancano i vari comandi da spedire ad Xbee</p>
      </div>

    )
  }
}

export default Xbee;