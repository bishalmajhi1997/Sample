// set():It does not allow wrong and bad values..validation it is wrong.
// get()...it is used to manupulate and calculate.
class Person {
    // properties
    #personName;
    #Age;
    // constructor(pname,page){
    //     this.#personName=pname;
    //     this.#Age=page;
    // }
    // setPersonName()
    setPersonName(value) {
        if (value == null || value == undefined) {
            console.error("null and undefined not allowed for personname");
        }
        else {
            if (value.length >= 30) {
                console.error("Personname should be more than 30 charecters.")
            }
            else {
                this.#personName = value;
            }
        }
    }
    // getPersonName()
    getPersonName() {
        return this.#personName;
    }
    // setAge()
    setAge(value) {
        if (value >= 0 && value <= 100) {
            this.#Age = value;
            // return this.#Age;
        }
    }
    // getAge()
    getAge() {
        return this.#Age;
    }
}
var person1 = new Person();
console.log(person1)
person1.setPersonName("bishal")
console.log(person1.getPersonName())
person1.setAge(50);
// console.log(person1.setAge(30));
console.log(person1.getAge())
