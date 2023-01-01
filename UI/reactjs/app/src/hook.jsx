import React,{useState,useEffect} from 'react'

export default function Hook() {
    const [count,setCount]=useState(0)
    const increment=()=>{
        setCount(count+1)
    }
    const decrement=()=>{
        setCount(count-1)
    }
    useEffect(()=>{
        document.title=`You clicked ${count} times`
    })
    const Click=()=>{
        setCount(count+1)
    }


    return (
        <div>
        <button onClick={increment}>+</button>
        <span>{count}</span>
        <button onClick={decrement}>-</button>
        <br />
        <p>You clicked {count} times</p>
        <button onclick={Click}>Click me</button>

        </div>
    )
}
