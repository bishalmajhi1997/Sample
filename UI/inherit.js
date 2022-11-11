// parent class
class Teacher {
    teachername;
    constructor(tname) {
        this.teachername = tname;
    }
}
//   child class
class PhysicsTeacher extends Teacher {
    mainSubject;
    constructor(msubject, cityname) {
        super(cityname);//parent class constructor
        this.mainSubject = msubject;
    }
    getDetails() {
        return `teachername:${this.teachername},mainSubject:${this.mainSubject}`;
    }
}
let teacher1 = new Teacher("allen");
console.log(teacher1);

let PhysicsTeacher1 = new PhysicsTeacher("Javascrippts", "john");
console.log(PhysicsTeacher1);
console.log(PhysicsTeacher1.getDetails());

    //   child class
//Polymorphism
//parent class
class Person{
    personName;
    personAge;
    constructor(pname,page){
        if(this.constructor==Person){
            throw new Error("Abstract class cannot be access")
        }
        this.personName=pname;
        this.personAge=page;
    }
    getDetails1(){
        return `PersonName:${this.personName},PersonAge:${this.personAge}`;
    }
}
class Teacher23 extends Person{
    mainSubject1;
    constructor(msubject1,pname,page){
        super(pname,page);
        this.mainSubject1=msubject1;
        // super(pname,page);
    }
    tgetDetails(){
        return `${super.getDetails1()},Subjectname:${this.mainSubject1}`;
    }


}
// let person1=new Person("bishal,25");
// console.log(person1)
let person2=new Teacher23("Html","Sumit",26);
console.log(person2);
console.log(person2.tgetDetails());
// console.log(person1.getDetails1());
// class Person
// {
//     personName;
//     Age;
//     constructor(pname,page)
//     {
//         this.personName=pname;
//         this.Age=page;
//     }
//     pgetDetails()
//     {
//         return `personname: ${this.personName},age: ${this.Age}`;
//     }
// }
// class Teacher extends Person
// {
//    mainSubject;
//    constructor(msubject,pname,page)
//    {
//       super(pname,page);  // invoves parents class const
//       this.mainSubject=msubject;
//    }
//    cgetDetails()
//    {
//      return `${super.pgetDetails()},mainsubject: ${this.mainSubject}`;
//    }
// }
// let person1=new Person("naidu",34);
// console.log(person1);
// console.log(person1.pgetDetails());
// let teacher2=new Teacher("maths","allen",23);
// console.log(teacher2);
// console.log(teacher2.cgetDetails());

