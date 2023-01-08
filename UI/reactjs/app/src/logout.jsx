import React, { Component } from 'react'

export default class Logout extends Component {
    state={
        numbers:[1,2],
        users:[{id:123,names:"ravi"},
              {id:124,names:"raju"},
               {id:125,names:"raji"}]
    }
  render() {
    const lists=this.state.numbers.map((num)=><li key={num}>{num}</li>)
    const userlists=this.state.users.map((users)=><li key={users.id}>{users.id} names is :{users.names}</li>)
    return (
      <div>Signout
       <ul>
        <li>{lists}</li>
       </ul>
       <ul>
        <li>{userlists}</li>
       </ul>
        
      </div>
    )
  }
}
