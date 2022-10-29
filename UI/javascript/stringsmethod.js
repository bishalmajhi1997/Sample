// string
// 1.length
var len="abcdefghijklmnopqrstuvwxyz"
console.log(len.length);
// 2.slice
var sli="sumit,ray,haguri,muturi"
sl=sli.slice(3,9);
console.log(sl);
sl2=sli.slice(-9)
console.log(sl2);
sl3=sli.slice(-3,-8);
// substring,substr,replace,tolowercase,touppercase,trim.trimstart,trimend,padstart,tostring,padend,charat,charcodeat,
// substring
var sub="mango,jwice,sweet potato,dal,ice cream"
var sub=sub.substring(3,9);
console.log(sub);
var mu=sub.substr(3,8);
console.log(mu);
// sub.replace("dal",88);
// console.log(sub);
sub="Please visit microsoft offices."
var mu=sub.replace("visit","click the picture of")
console.log(mu);
// toLowerCase
var mmu=sub.toLowerCase();
console.log(mmu);
// toUpperCase
var mmm=sub.toUpperCase();
console.log(mmm);
// concat
var co=mmu.concat(" ",mmm)
console.log(co);
text = "Hello" + " " + "World!";
text = "Hello".concat(" ", "World!");
console.log(text)
// trim,trimstart,trimend
var tr="     You are awesome..    "
console.log(tr.trim())
console.log(tr.trimStart())
console.log(tr.trimEnd())
// pad,padstart,padend
var num=4;
// var k=num.padStart(3,"x");
// console.log(k)
// var m=5 there  padstart,padend is not supported chrome.
// var k=k.padEnd(3,"2")
// console.log(k)
var nn=num.toString()
console.log(nn);
// charat
var ch=text.charAt(3);
console.log(ch);
// charcodeat
var ch=text.charCodeAt(3);
console.log(ch);
var text2=" abhi is good girl sumit is bad boy"
t=text2.split("|");
console.log(t);

