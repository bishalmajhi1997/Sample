// // Type scriptings.
// var greet: string = "Greetings";
// var geeks: string = "GeeksforGeeks";
// console.log(greet + " from " + geeks);
function sum() {
    console.log("india");
}
sum();
var x = 1000;
function sum() {
    var a = 200, b = 300;
    var c = a + b;
    console.log(c)
}
sum()
// console.log(a) error
console.log(x)
function sum1(a, b) {
    var c = a + b;
    console.log(c)
}
sum1(10, 20)
function sum2(a, b){
    var d = a + b;
    console.log(d)
    console.log(arguments[5])
    console.log(arguments[9])
    console.log(arguments.length)

}
sum2(20, 30, 40, 50, 60, 80)
//function with return keyword
function add(x, y) {
    var z = x + y;
    return z;
}
var result = add(25, 30);
console.log(result);

function test1(a){
    return a;
}
console.log(test1(888));
//functions expression
var test2=function(a){
    return a;
}
console.log(test2(300))
//arrow function
var test3=a=>a;//no return values;
console.log(test3(600));
var test4=(s,t)=>{return s+t;};
console.log(test4(290,300));
//reverse the string in js?
