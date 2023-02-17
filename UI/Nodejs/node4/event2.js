const e1=require('events')
var e2=new e1.EventEmitter();
e2.on('ABC',()=>{
    console.log("hello event TWO")
})
e2.emit('ABC')