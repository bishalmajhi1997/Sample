
import React, { Component } from "react";
import { Link, Outlet } from 'react-router-dom';
import Carousel from 'react-bootstrap/Carousel';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';



class NavBar extends Component {
  render() {
    return (
      <div>
            <Carousel>
      <Carousel.Item>
      <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
      <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
      <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>

      </Carousel.Item>
    </Carousel>

            <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowstyle.com/wp-content/uploads/2015/01/home-design-interior-design-kitchen-designer-kitchens-461-4140x2755.jpg" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
            <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowstyle.com/wp-content/uploads/2015/01/home-design-interior-design-kitchen-designer-kitchens-461-4140x2755.jpg" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>

        <Carousel>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src="https://tse2.mm.bing.net/th?id=OIP.2cexaSk7Zy7jiD2a3aYJ6gHaJ4&pid=Api&P=0"
              alt="First slide" height="500px" width="500px"
            />
            <Carousel.Caption>
              <h3>First slide label</h3>
              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src="https://i5.walmartimages.com/asr/2b4770d0-166d-47e0-b8ad-a04d4e8836f6_1.d44afd19b420cda13c58da42c38e95b9.jpeg"
              alt="Second slide" height="500px" width="500px"
            />

            <Carousel.Caption>
              <h3>Second slide label</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              className="d-block w-100"
              src="https://images-na.ssl-images-amazon.com/images/I/61oxoVqDSbL._AC_UX679_.jpg"
              alt="Third slide" height="500px" width="500px"
            />

            <Carousel.Caption>
              <h3>Third slide label</h3>
              <p>
                Praesent commodo cursus magna, vel scelerisque nisl consectetur.
              </p>
            </Carousel.Caption>
          </Carousel.Item>
        </Carousel>

        <nav className="navbar navbar-expand-lg bg-info">
          <div className="container-fluid">
            <a className="navbar-brand" href="#/">
            </a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <Link className="nav-link active" aria-current="page" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/Dashobard">DashBoard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/Customer">CustomerList</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/ShoppingCart">ShoppingCart</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/SignUp">Signup</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/Login">Login</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/Images">Images</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/Customerlist">Customerlist</Link>
                </li>
                <li className="nav-item dropdown">
                  <a className="nav-link dropdown-toggle" href="#/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Dropdown
                  </a>
                  <ul className="dropdown-menu">
                    <li><a className="dropdown-item" href="#/">Action</a></li>
                    <li><a className="dropdown-item" href="#/">Another action</a></li>
                    <li><hr className="dropdown-divider" /></li>
                    <li><a className="dropdown-item" href="#/">Something else here</a></li>
                  </ul>
                </li>
              </ul>
              <form className="d-flex" role="search">
                <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                <button className="btn btn-outline-success" type="submit">Search</button>
              </form>
            </div>
          </div>
        </nav>
        <Outlet />
        <div className="row">
          <div className="col-4"> <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card></div>
          <div className="col-4"> <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card></div>
          <div className="col-4"> <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="http://thewowshttp:" />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card></div>
        </div>
        
      </div>
    )
  }
}
export default NavBar;









// import { Component } from "react";
// class NavBar extends Component
// {
//     render(){
//         return(
//             <nav className="navbar navbar-expand-lg bg-info">
//     <div className="container-fluid">
//       <a className="navbar-brand" href="/#">Navbar</a>
//       <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
//         <span className="navbar-toggler-icon"></span>
//       </button>
//       <div className="collapse navbar-collapse" id="navbarSupportedContent">
//         <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//           <li className="nav-item">
//             <a className="nav-link active" aria-current="page" href="/#">Home</a>
//           </li>
//           <li className="nav-item">
//             <a className="nav-link" href="/#">Link</a>
//           </li>
//           <li className="nav-item dropdown">
//             <a className="nav-link dropdown-toggle" href="/#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
//               Dropdown
//             </a>
//             <ul className="dropdown-menu">
//               <li><a className="dropdown-item" href="/#">Action</a></li>
//               <li><a className="dropdown-item" href="/#">Another action</a></li>
//               <li><hr className="dropdown-divider"/></li>
//               <li><a className="dropdown-item" href="/#">Something else here</a></li>
//             </ul>
//           </li>
//           <li className="nav-item">
//             <a className="nav-link disabled" href='/#'>Disabled</a>
//           </li>
//         </ul>
//         <form className="d-flex" role="search">
//           <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
//           <button className="btn btn-outline-success" type="submit">Search</button>
//         </form>
//       </div>
//     </div>
//   </nav>
//         )
//     }
// }
// export default NavBar;
