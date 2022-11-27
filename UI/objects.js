// var objectname={
//     // properties;
//   key:values
//     // methods;
// };
var std = {
    //  properties
    sno: 101,
    sname: "ravi",
    smarks: [10, 20, 30, 40, 90],
    saddress: {
        ph: 999282,
        float: 1992.9,
        string: "ndnd",
    }


};
var emp = {
    empno: 111, 
    empname: "sbshhs",
     empsal: 29992, 
     empdes: 'software',
     empaddres:
     {
        dr:999,
        float:77.99,
        street:"mango",
     }
};
console.log(std)
console.log(emp)
console.log(std.sno)
console.log(emp.empno)
console.log(emp.empaddres.street)
// delete
delete(emp.empname)
// for-in loop
for(E in emp){
    console.log(`${E} is ${emp[E]}`)
}
// n.b: `:tactics
for(i in std){
    console.log(`${i} in ${std[i]}`)
}
for (k in emp){
    console.log(k)
    if(k==emp.empaddres){
        for(k1 in emp.empaddres){
            console.log(`${k1} is ${emp.empaddres[k1]}`)
        }
    }
    else{
         console.log(`${k} is ${emp[k]}`)
    }
}
console.log(" ")
// objects with methods
var std={
    // properties
    fname:"ravi",
    lname:"kumar",
    // methods
    fullname:function(){
        // this.fname;
        // this.lname
        console.log(this.fname+" "+this.lname);
    }

}
var result=std.fullname();
// console.log(result)