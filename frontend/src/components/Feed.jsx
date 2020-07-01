import React, {Component} from 'react';
import $ from 'jquery';


class Feed extends Component{
    constructor(props){
        super();
        this.state ={
            post: [],
            searchField: ''
        }
    }

    componentDidMount(){
        $.ajax({
            url:`/post`,
            type:"Get",
            success:(result) =>{
                this.setState({post: result.posts})
                return;
            },
            error: (error) =>{
                alert('Unable to fetch posts from Api')
                return;
            }
        })
    }
}