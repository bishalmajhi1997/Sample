import { Component } from 'react';
import car from './images/car.jpg';
import car2 from './images/car2.jpg';

class Images extends Component{
    render(){
        const styles={
            headings:{height:"300px",
                      width:"500px"}
        }
        return (
            <div>
             <img src={car} alt="this is car"  style={styles.headings}/>
             <img src={car2} alt="this is car2"  style={styles.headings}/>
            </div>
        )
    }
}
export default Images;