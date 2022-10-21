// conditions control statements:if,if..else,else if,nested if,switch case
// == :compare with values
// ===:compare value along with datatypes
// simple if
var a = 20;
if (a == 20) {
    console.log("a is equal to b");
}
// simple if-else:
var b = 200;
if (b == 200) {
    console.log("b is equal to 200");
}
else {
    console.log("b is not equal to 200");
}
// else if
var x = 10;
if (x != 10) {
    console.log("x==10");
}
else if (x < 10) {
    console.log("x is wrong statement");
    }
    else {
    console.log("x=10");
    }

//Nested if
//switch case
var monthname;
var monthnumber=14;
switch(monthnumber){
    case 1:monthname="january";
    break;
    case 2:monthname="Feb";
    break;
    case 3:monthname="Mar";
    break;
    case 4:monthname="Apr";
    break;
    case 5:monthname="May";
    break;
    case 6:monthname="jun";
    break;
    case 7:monthname="jul";
    break;
    case 8:monthname="Aug";
    break;
    case 9:monthname="Sept";
    break;
    case 10:monthname="Oct";
    break;
    case 11:monthname="Nov";
    break;
    case 12:monthname="Dec";
    break;
    default:monthname="invalid monthl";
    break;
}

console.log(monthname);
// looping statements:for loop while,do..while
// while
var i=0;//initialization
while (i<=10){//test condition
    console.log("hello js",i);
    i++;//i=i+1 //iterartion statements
}
// do..while loop
var j=0;
do{
    console.log("hello js",j);
    j++;
}
while(j<=5);
// for loop
for(var k=0;k<5;k++){
    console.log("hello js",k);
}
for(var i=1;i<=10;i++){
     document.write("2*"+i+"="+2*i+"<br>")
}
// var fact=5;
// for(var i=1;i<=5;i++){
//      fact*=i;
//      console.log(fact)
// }