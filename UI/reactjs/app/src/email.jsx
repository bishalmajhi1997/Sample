import React,{useState} from 'react';
import emailjs from "@emailjs/browser"

export default function email1() {
    const[data,setData]=useState({
        username:"",
        password:""
    })
    const {username,password}=data;
    const changeHandler=e=>{
      setData({...data,[e.target.name]:[e.target.value]})
    }
    const submitHandler=e=>{
      e.preventDefault()
      console.log(data)
      emailjs.sendForm('service_vsf32e1', 'template_qb8ec2o',e.target, 'dHJP1N9D_hSyVXwiF')
    .then((result) => {
        console.log(result.text);
    }, (error) => {
        console.log(error.text);
    });
    }
  return (
    <div>
        <h1>Email page</h1>
        <form action="#" onSubmit={submitHandler}>
          <input type="text" name="username" id="u" value={username} onChange={changeHandler}/><br />
          <input type="password" name="password" id="p" value={password} onChange={changeHandler} /><br />
          <input type="submit" value="submit" />
        </form>
    </div>
  )
}
