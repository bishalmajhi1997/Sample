class Emp{
    // properties
    empName;
    empAge;
    empSalary;
    // methods
    getEmpName(){
        return this.empName;
    }
    hikeSalary(amount){
        this.empSalary=this.empSalary+amount;
        return this.empSalary;
    }
}
// object creations
let emp1=new Emp();
emp1.empName="Hari";
emp1.empAge=26;
emp1.empSalary=60000;
console.log(emp1);
console.log(emp1.empName);
let emp2=new Emp();

emp2.empName="Moulali";
emp2.empAge=24;
emp2.empSalary=60000;
emp2.hikeSalary(20000);
console.log(emp2.hikeSalary(1000))
// Contructor is a special function in oops concepts and decleared within arguments.
class Employee{
    //properties
    empName;
    #empAccount;
    // #:indicates private property.
    empAge;
    empDes;
    // construtor
    constructor(pname,page,pdes,pacc){
         this.empName=pname;
         this.#empAccount=pacc
         this.empAge=page;
         this.empDes=pdes;

    }
    // methods
    getEmpDetails(){
        return this.#empAccount;
    }
}
let emp3=new Employee("moulali",24,"Developer");
let emp4=new Employee("Ajit",27,"Senior Developer",300000);
console.log(emp3,emp4)
console.log(emp4.getEmpDetails())