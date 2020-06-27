import React, {Component} from 'react';

class Header extends Component{

    render(){
        return (
            <div className="App-header">
                <h1 onClick={() => {this.navTo('')}}>Udacitrivia</h1>
                <h2 onClick={() => {this.navTo('')}}>List</h2>
                <h2 onClick={() => {this.navTo('/add')}}>Add</h2>
                <h2 onClick={() => {this.navTo('/play')}}>Play</h2>
            </div>
        );
    }
}

export default Header;