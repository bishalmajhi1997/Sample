// BOM:Browser object model
// 1.window...alert,confirm,prompt,open,size,setinterval,settimeout
// 2.history..back,forward,screen,navigater

// alert("hello alert")
// confirm("hello confirm")
function open1(){
    open("https://www.google.com");
}
function close1(){
    close();
}
// size
var x=window.innerWidth;
var y=window.innerHeight;
document.write(x+" "+y)
function hello(){
    alert("hello levelup")
}
// setInterval(hello,200)
// setTimeout(hello,2000)
document.write(navigator.platform+"<br>");
document.write(navigator.languages+"<br>");
document.write(navigator.clipboard+"<br>");
document.write(navigator.appName+"<br>");
document.write(screen.height+"<br>");
document.write(screen.clipboard+"<br>");
document.write(screen.width+"<br>");
function prompt1(){
    var p=prompt();
    document.write("p");
}


// scren:screen.heigh,screen.width,screen.pixeldepth,screen.solorDepth
// navigator:appName,appVersion,appCodeName,CookieEnabled,userAgent,language,product,javaEnabled()