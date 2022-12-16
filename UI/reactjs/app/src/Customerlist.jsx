import  { Component } from "react";

class Customerlist extends Component{
   constructor(props){
           super(props);
           this.state={color:"red", bgcolor:"green"}
   }
   ChangeColor=()=>{
                   this.setState({color:"blue"});
   }
   render(){
    return(
        <div>
            <h1 className="text-danger">{this.state.color}</h1>
            <Second color={this.state.color}/>
            <button type="button" className="btn btn-info" onclick={this.ChangeColor}>Change color</button>
        </div>
    )
   }
}
class Second extends Customerlist{
    render(){
        return(
            <div>
                <h2>{this.props.color}</h2>
            </div>
        )
    }
}
export default Customerlist;