import { Component } from "react"
import Home from "./home";
class Dashobard extends Component{
    render(){
        return(
            <div>
                <Home name={this.props.title}/>
            <h1>Dashboard Lorem ipsum dolor sit amet consectetur adipisicing elit. Iusto hic laudantium fuga odio, eum cupiditate quos?</h1>
            </div>
        )
    }
}
export default Dashobard;