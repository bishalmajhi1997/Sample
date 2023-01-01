import React, {useState,useEffect} from 'react'
const URL="https://jsonplaceholder.typicode.com/users";
export default function Reactts() {
  const [usersData,setUsersData]=useState([]);
  const fetchUserData= async(apiURL)=>{
    const response =await fetch(apiURL);
    console.log("data", response);
    const data= await response.json();
    // console.log(data);
    setUsersData(data);
  }
  useEffect(()=>{
    fetchUserData(URL);
  })
   return (
    <div>
      <h1>useEffect page</h1>
      <ul>
        {usersData.map((eachUser)=>{
          const {id,name,email}=eachUser;
          return(
            <li key={id}>
              <div>{id}</div>
              <div>{name}</div>
              <div>{email}</div>
            </li>
          );
        })}
      </ul>
    </div>
  )
};






