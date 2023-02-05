var h1=require('http')//hyper text transfer protocol
h1.createServer((req,res)=>{
    res.write('hello world');
    res.end();//ending the response
}).listen(3000);//localhost:3000
