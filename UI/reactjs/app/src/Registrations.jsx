import React, { useState } from 'react'

export default function Registrations() {
    const [data, setData] = useState(
        {
            email: '',
            password: '',
            address: '',
            city: '',
            state: '',
            zip: '',
        }
    )
    const { email, password, address, city, state, zip } = data;
    const changeHandler = e => {
        setData({ ...data, [e.target.name]: [e.target.value] })
    }
    const submitHandler = e => {
        e.preventDefault()
        console.log(data)
    }

    return (
        <form onSubmit={submitHandler}>
            <div className="form-row">
                <div className="form-group col-md-6">
                    <label for="inputEmail4">Email</label>
                    <input type="email" className="form-control" id="inputEmail4" placeholder="Email" name="email" value={email} onChange={changeHandler} />
                </div>
                <div className="form-group col-md-6">
                    <label for="inputPassword4">Password</label>
                    <input type="password" className="form-control" id="inputPassword4" placeholder="Password" name="password" value={password} onChange={changeHandler} />
                </div>
            </div>
            <div className="form-group">
                <label for="inputAddress">Address</label>
                <input type="text" className="form-control" id="inputAddress" placeholder="1234 Main St" name="address" value={address} onChange={changeHandler} />
            </div>
            <div className="form-row">
                <div className="form-group col-md-6">
                    <label for="inputCity">City</label>
                    <input type="text" className="form-control" id="inputCity" name="city" value={city} onChange={changeHandler} />
                </div>
                <div className="form-group col-md-4">
                    <label for="inputState">State</label>
                    <select id="inputState" className="form-control" name="state" value={state} onChange={changeHandler}>
                        <option selected>Choose from these</option>
                        <option>Telangana</option>
                        <option>Andhra Pradesh</option>
                        <option>Madhya Pradesh</option>
                        <option>Goa</option>
                        <option>Kerala</option>
                    </select>
                </div>
                <div className="form-group col-md-2">
                    <label for="inputZip">Zip</label>
                    <input type="text" className="form-control" id="inputZip" name="zip" value={zip} onChange={changeHandler} />
                </div>
            </div>
            <div className="form-group">
                <div className="form-check">
                    <input className="form-check-input" type="checkbox" id="gridCheck" />
                    <label className="form-check-label" for="gridCheck" required>
                        *Privacy and Terms
                    </label>
                </div>
            </div>
            <button type="submit" className="btn btn-primary">Sign Up</button>
        </form>
    

    )
}
