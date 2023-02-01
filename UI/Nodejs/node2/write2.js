var f1=require('fs')
// f1.writeFile('file1.txt',"manho\nssss\nnoshjsjjdes",()=>{console.log('I have writing something.')})
var b=f1.writeFileSync('file1.txt',"react");
console.log(b)
