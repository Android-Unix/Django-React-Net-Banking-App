import React from 'react';
import { Component } from 'react'
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
    console.log('Inside App Constructor');
  }
  // async componentDidMount() {
  //   const data = await fetch('http://localhost:8000/list-accounts/')
  //   console.log(data.json());
  // }

  render(){
    return (
      <div className="App">
        <h1>Welcome Netbanking</h1>
      </div>
    );
  }
}
 
 
export default App;
