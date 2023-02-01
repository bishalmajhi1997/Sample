var f1=require('fs')
f1.readFile('file1.txt','utf-8',(err,data)=>{console.log(err,data)})
f1.readFile('file1.txt','utf-8',(err,data)=>{if(err){
    console.log(err);

}
else{
    console.log(data);
}})