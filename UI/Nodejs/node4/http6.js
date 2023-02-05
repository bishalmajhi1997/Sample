var h1 = require('http');
var h2=require('fs')
var p1 = process.env.PORT || 3000;
var server = h1.createServer((req, res) => {
    if (req.url == '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/html')
        var e=h2.readFileSync('class5.html','utf-8')
        req.statusCode = 200
        res.write(e)
        res.write("<h2>First Page</h2>");
    }
    else if (req.url == '/about') {
        res.setHeader('Content-Type', 'text/html')
        var a="bishal"
        var d=h2.readFileSync('class5.html','utf-8')
        req.statusCode = 200
        // res.write("<h2>About page</h2>"+a);
        res.write(d)
        res.write("<h2>About page</h2>"+a);

    

    }
    else {
        res.setHeader('Content-Type', 'text/html')
        res.write('<h3>Page not found</h3>')
    }
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