// var h1=require('http');
// h1.createServer((req,res)=>{
//      res.write("Hello world")
//      res.end();
// }).listen(8080);

var h1=require('http');
var p1=process.env.PORT||3000
var server=h1.createServer((req,res)=>{
    if (req.url=="/"){
        res.statusCode=200
        res.setHeader('Content-Type','text/html')
        res.write("<h3>hello bevit</h3>")
    }
    else if (req.url=="/about"){
        res.statusCode=200
        res.setHeader('Content-Type','text/html')
        res.write("<h3>hello bishal</h3>")
    }
    else{
        res.setHeader('Content-Type','text/html')
        res.write('hello khushhh')
    }

     res.write("Hello world")
     res.end();
})
server.listen(`${p1}`)
