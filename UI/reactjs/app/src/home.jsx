import { Component } from "react";

class Home extends Component{
    state={
        title:"welcome to home",
        color:"black"
    }
    render(){
        return(
            <div>
            <h1  class="display-1 text-center bg-primary text-danger">{this.state.title}</h1>
            <h1  class="display-1 text-center bg-primary text-danger">{this.state.color}</h1>
            </div>
        )
    }
}
export default Home;