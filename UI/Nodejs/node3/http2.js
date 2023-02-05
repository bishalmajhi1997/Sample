var h1=require('http');
var p1=process.env.PORT || 3000;
var server=h1.createServer((req,res)=>{
    res.setHeader('Content-type','text/html')
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.write("<h2>Hello world</h2>");
    res.end();
})
server.listen(`${p1}`);
console.log(`${p1}`)