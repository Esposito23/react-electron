import React, { Component } from 'react';
import '../../App.css'

class Lineare extends Component {

  constructor(props) {
    super(props)
    this.state = {
      stato: 'Motore Lineare Fermo'
    }
  }
  LineareOn = () => {
    fetch('/linearHome')
      .then(res => res.json())
      .then(mess => {
        this.setState({ stato: mess.stato });
      })
  }
  LineareAway = () => {
    fetch('/linearAway')
      .then(res => res.json())
      .then(mess => {
        this.setState({ stato: mess.stato });
      })
  }
  LineareStop = () => {
    fetch('/linearStop')
      .then(res => res.json())
      .then(mess => {
        this.setState({ stato: mess.stato });
      })
  }


  render() {
    return (
      <div className='App-header'>
        <h1>Motore Lineare</h1>
        <p>{this.state.stato}</p>
        <row>
        <button onClick={this.LineareOn}>Home</button>
        <button onClick={this.LineareAway}>Away</button>
        <button onClick={this.LineareStop}>Stop</button>
        </row>
      </div>

    )
  }
}

export default Lineare;