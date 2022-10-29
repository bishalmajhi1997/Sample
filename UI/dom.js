function getname(){
    var fname=document.form1.name.value;
    alert(fname)
}
function getcube(){
    var num=document.getElementById("x").value;
    alert(num*num*num);
}
function total(){
    var totalgenders=document.getElementsByName("gender");
    alert("totalgenders:"+totalgenders.length);
}
function countpara(){
    var totalpara=document.getElementsByTagName("p");
    alert("total paragraph"+totalpara.length)
}
function changered(){
    document.getElementById("demo").style.color="red";
}
function changeblue(){
    document.getElementById("demo").style.color="blue";
}
function changecolor(){
    var c=prompt();
    document.getElementById("demo").style.color=c;
    // prompt 
}
function c(){
    var c=document.getElementsByClassName("a");
    document.write("this is class+<br>"+c);
}
function img(){
    document.getElementById("img").src="https://images.hdqwalls.com/wallpapers/batman-arkham-knight-2015.jpg"
}
// BOM:Browser object model
// 1.window...alert,confirm,prompt,open,size,setinterval,settimeout
// 2.history..back,forward,screen,navigater
