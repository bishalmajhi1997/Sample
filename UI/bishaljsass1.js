// if condition
var marks = 85;
if (marks <= 100 && marks >= 90) {
    console.log("Grade o")
}
else if (marks >= 80 && marks < 90) {
    console.log("grade e")
}
else if (marks >= 70 && marks < 80) {
    console.log("grade a")
}
else if (marks >= 60 && marks < 70) {
    console.log("grade b")
}
else if (marks >= 50 && marks < 60) {
    console.log("grade c")
}
else if (marks >= 40 && marks < 50) {
    console.log("grade d")
}
else if (marks >= 35 && marks <40) {
    console.log("grade p")
}
else{
    console.log("fail");
}
// switch cases
var grade;
var marks=99;
switch(true){
    case (marks <=100 && marks >90):
       var grade="grade O";
        break;
    case(marks >=80 && marks<90):
    var grade="grade E";
    break;
    case(marks >=70 && marks<80):
    var grade="grade A";
    break;
    case(marks >=60 && marks<70 ):
    var grade="grade B";
    break;
    case(marks >=50 && marks<60):
    var grade="grade C";
    break;
    case(marks >=40 && marks<50):
    var grade="grade D";
    break;
    case(marks>=35 && marks<40):
    var grade="grade P";
    break;
    default:
    var grade="Fail";
    break;
}
console.log(grade)