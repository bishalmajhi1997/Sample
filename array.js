var x;//declrattion
var num=[100,200,300,400];//initialization
var srg=["moulali","bishaal","ajhit"];
console.log(num);
console.log(srg);
console.log(num.length);
console.log(srg.length);
console.log(num[0]);
console.log(srg[2]);
// 3 types of array:
//1. array literal
var student=['shuvangi',1,"abhi","monika",'bramhanaidu']
console.log(student)
for(i=0;i<student.length;i++){
    console.log(student[i]);
}
//2.array directly
var std=new Array();
std[0]="suresh";
std[1]="gayatri";
std[2]=3;
std[3]="4";
std[5]="lo";
console.log(std);
var j=0;
while(j<std.length){
    console.log(std[j],j);
    j++;

}
//3. array constructor
var emp=new Array("30000",40000,50000,"bishal");
console.log(emp)
for(var i=0;i<emp.length;i++){
    console.log(emp[i])
}
var i=0;
while(i<emp.length){
    console.log(emp[i]);
    i++;
}
// array methods
// 1.push()
var num=[10,20,30,40];
num.push(50,60);
console.log("after push:",num);
// 2.unshift
num.unshift(8,9);
console.log("After unshift:",num);
// 3.pop
num.pop();
console.log("after pop (end):",num);
// 4.shift
num.shift();
console.log("after shift(begin):",num);
// 5.splice
num.splice(1,2);
console.log("after splice(index position:):",num);
num.splice(1);
console.log("after splice",num);
// 6.sort()
num.push(20,30,10,30,29,29,99,19,18);
console.log(num);
num.sort();
console.log("after sort:",num);
// 7.reverse()
num.reverse();
console.log("after reverse:",num);
// rest opeartor
function add(a,...b)//rest opearator(...)
{
    console.log(a);
    console.log(b);
}
add(20,30,40,10,20,30,40,77,99);
// for of loop
var statement=["ram","laxman","sita"]
for(var x of statement){
    console.log(x);
}
// filter
var x;
var num1=[100,200,300]
var result=num1.filter((x)=>(x>100));
console.log(result);
var num2=[100,200,"bishal"]
k=num2.toString()
console.log(k);
m=num2.join(" # ")
console.log(m);
// map
var num11=[100,200,300,400]
var result=num11.map(x=>x*100)
console.log(result);
// concat
var num22=[11,33]
var w=num22.concat(num11)
console.log(w)