import React,{useState} from 'react'

export default function Hook() {
    const [count,setCount]=useState(0)
    const increment=()=>{
        setCount(count+1)
    }
    const decrement=()=>{
        setCount(count-1)
    }


    return (
        <div>
        <button onClick={increment}>+</button>
        <span>{count}</span>
        <button onClick={decrement}>-</button>

        </div>
    )
}
