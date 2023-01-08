import React,{ Component } from "react";
// import Footer from "./footer";
// import MainContent from "./MainContent";
import NavBar from "./NavBarr";
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import Home from "./home"
// import Dashobard from "./dashboard";
import Customer from "./customer";
import ShoppingCart from "./ShoppingCart";
import PageNotFound from "./pagenotfound";
import SignUp from "./signup";
import Login from "./login";
import Images from "./image";
import Customerlist from "./Customerlist.jsx"
import Angular from "./Angular";
import React1 from "./React";
import Technologies from "./Technologies";
import Hook from "./hook";
import Reactts from "./api"
import Signup1 from "./Signup1.jsx";
import Registrations from "./Registrations";
import Logout from "./logout";

const Lazycustom= React.lazy(() => import('./dashboard'));

class App extends Component{
    render(){
        return(
            <BrowserRouter>
                 <h1 class="text-danger text-center bg-info">LEVELUP</h1>
                 <Routes>
                    <Route path="/" element={<NavBar/>}>
                        <Route index element={<Home/>}></Route>
                        <Route path="/Dashobard" exact element={
                            <React.Suspense fallback="loading..."><Lazycustom/></React.Suspense>
                        }></Route>
                        <Route path="/Customer" exact element={<Customer/>}></Route>
                        <Route path="/ShoppingCart" exact element={<ShoppingCart/>}></Route>
                        <Route path="/SignUp" exact element={<SignUp/>}></Route>
                        <Route path="/Signup1" exact element={<Signup1/>}></Route>
                        <Route path="/Login" exact element={<Login/>}></Route>
                        <Route path="/Images" exact element={<Images/>}></Route>
                        <Route path="/Customerlist" exact element={<Customerlist/>}></Route>
                        <Route path="/Pagenotfound" exact element={<PageNotFound/>}></Route>
                        <Route path="/Hook" exact element={<Hook/>}></Route>
                        <Route path="/Logout" exact element={<Logout/>}></Route>
                        <Route path="/Registrations" exact element={<Registrations/>}></Route>
                        <Route path="/Reactts" exact element={<Reactts/>}></Route>
                        <Route path="/Technologies" exact element={<Technologies/>}>
                            <Route path="React1" exact element={<React1/>}></Route>
                            <Route path="Angular" exact element={<Angular/>}></Route>
                        </Route>
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
