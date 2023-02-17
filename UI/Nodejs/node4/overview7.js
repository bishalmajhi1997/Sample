var  h1=require("http")
var port=process.env.port || 3000;
h1.createServer((req,res)=>{
    console.log("hello")
}).listen(`${port}`)