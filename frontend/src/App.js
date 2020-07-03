import React, { Component } from 'react';
import logo from './logo.svg';
import './stylesheets/App.css';
import Header from './components/Header';
import {
  BrowserRouter as Router,
  Route, 
  Switch
} from 'react-router-dom'

class App extends Component{
  render(){
    return(
      <div className ="App">
        <Header path/>
        <Router>
          <Switch>
            <Route path="/"/>
            <Route path="/profile"/>
            <Route path="/feed"/>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;