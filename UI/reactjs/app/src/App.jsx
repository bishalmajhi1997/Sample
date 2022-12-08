import React,{ Component } from "react";
import Footer from "./footer";
import MainContent from "./MainContent";
import NavBar from "./NavBarr";


class App extends Component{
    render(){
        return(
            // <h1>hello</h1>
            <React.Fragment>
                <NavBar/>
                <MainContent/>
                <Footer/>
            </React.Fragment>
            // <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste aliquam quo perferendis ut, minus dicta voluptatum ex officiis quasi voluptate.</p>
        )
    }
}
export default App;






// import React, { Component } from "react";
// import NavBar from "./NavBarr";
// import MainContent from "./MainContent";
// class App extends Component
// {
//   render(){
//     return(
//        <React.Fragment>
//         <NavBar/>
//        <MainContent/>
//        </React.Fragment>
// //       <div>
// //         <h1>hello fsd1</h1>
// //        <p>Lorem ipsum dolor sit amet.</p>
// //    <  /div>
//     )
//   }
// }
// export default App;
