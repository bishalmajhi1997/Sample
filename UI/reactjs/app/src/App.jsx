import React,{ Component } from "react";
// import Footer from "./footer";
// import MainContent from "./MainContent";
import NavBar from "./NavBarr";
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Home from "./home"
import Dashobard from "./dashboard";
import Customer from "./customer";
import ShoppingCart from "./ShoppingCart";
import PageNotFound from "./pagenotfound";
import SignUp from "./signup";
import Login from "./login";
import Images from "./image";
import Customerlist from "./Customerlist.jsx"
class App extends Component{
    render(){
        return(
            <BrowserRouter>
                 <h1 class="text-danger text-center bg-info">LEVELUP</h1>
                 <Routes>
                    <Route path="/" element={<NavBar/>}>
                        <Route index element={<Home/>}></Route>
                        <Route path="/Dashobard" exact element={<Dashobard/>}></Route>
                        <Route path="/Customer" exact element={<Customer/>}></Route>
                        <Route path="/ShoppingCart" exact element={<ShoppingCart/>}></Route>
                        <Route path="/SignUp" exact element={<SignUp/>}></Route>
                        <Route path="/Login" exact element={<Login/>}></Route>
                        <Route path="/Images" exact element={<Images/>}></Route>
                        <Route path="/Customerlist" exact element={<Customerlist/>}></Route>
                        <Route path="*" exact element={<PageNotFound/>}></Route>

                    </Route>
                 </Routes>
            </BrowserRouter>
            // <h1>hello</h1>
            // <React.Fragment>
            //     <h1 class="text-danger text-center bg-info">LEVELUP</h1>
            //     <NavBar/>
            //     <MainContent/>
            //     <Footer/>
            // </React.Fragment>
            // // <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste aliquam quo perferendis ut, minus dicta voluptatum ex officiis quasi voluptate.</p>
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
