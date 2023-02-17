const e1=require('events')
var e2=new e1.EventEmitter();
e2.on('waterfall',()=>{
    console.log("hello event")
})
e2.emit('waterfall')