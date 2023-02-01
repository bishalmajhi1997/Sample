var f1=require('fs')
f1.appendFile('file1.txt',"Django\ncss\nnodes",()=>{console.log('I have added the append line')})