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