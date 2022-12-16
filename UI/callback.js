// // function programing?-  higher order function and call back function
// // higher order function - function take as a arguments in higher order  function
// // call back func -passing func as a argument in higher order func
function bishal(a,b,task){
    let c=task(a,b);
    return c;
}
let res =bishal(10,20,function (a,b){
    return a+b;
})
console.log(res);

// // // let res1 =operation(10,10,function (a,b){
// // //     return a-b;
// // // })
// // // console.log(res1);

// // console.log( operation(10,10,function (a,b){return a*b;}));
// // // console.log(res);

// // console.log( operation(80,10,function (a,b){return a/b;}));

// // console.log( operation(10,10,function (a,b){return a%b;}));



// //🎇2nd way🎇- using 2 variable for all operation to display at a time

// // let variable can not reinitialize and redeclare

// // let a=Number(prompt("enter a "))
// // let b=Number(prompt('enter b '))


// // function operation(a,b,task){
// //     let c=task(a,b);
// //     return c;
// // }
// // let res =operation(a,b,function (a,b){
// //     return a+b;
// // })
// // console.log(res);

// // let res1 =operation(a,b,function (a,b){
// //     return a-b;
// // })
// // console.log(res1);

// // console.log( operation(a,b,function (a,b){return a*b;}));//callback function
// // // console.log(res);

// // console.log( operation(a,b,function (a,b){return a/b;}));

// // console.log( operation(a,b,function (a,b){return a%b;}));


// // 3rd way
// function operation(a,b,task){
//     let c=task(a,b);
//     return c;
// }
// let res =operation(a=Number(prompt("enter a ")),b=Number(prompt('enter b ')),function (a,b){
//     return a+b;
// })

// let res1 =operation(a=Number(prompt("enter a ")),b=Number(prompt('enter b ')),function (a,b){
//     return a-b;
// })

// let res2 =operation(a=Number(prompt("enter a ")),b=Number(prompt('enter b ')),function (a,b){
//     return a*b;
// })



// console.log(res);
// console.log(res1);
// console.log(res2);

