import React, {Component} from 'react';

class Form extends Component{
    render(){
        return(
            <div class="form">
                <form action="/profile" mehtods="get">
                Place: <input type="text" name="place"/>
                <input type="submit" value="Submit"/>
                </form>
            </div>
        );
    }
}

export default Form;
