import React, {Component} from 'react';
import '../stylesheets/Header.css';

class Header extends Component{

    render(){
        return (
            <div className="App-header">
                <h1 onClick={() => {this.navTo('')}}>Redeye</h1>
                <h2 onClick={() => {this.navTo('')}}>Feed</h2>
                <h2 onClick={() => {this.navTo('/add')}}>Profile</h2>
                <h2 onClick={() => {this.navTo('/play')}}>Play</h2>
            </div>
        );
    }
}

export default Header;