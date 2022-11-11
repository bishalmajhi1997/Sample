function validate() {
    var jname = document.getElementById("name").value;
    var jsubject = document.getElementById("Subject").value;
    var jphonenumber = document.getElementById("phone").value;
    var jmail = document.getElementById("em").value;
    var jmessage = document.getElementById("mes").value;
    var jerror_message = document.getElementById("error_message");
    jerror_message.style.padding = "10px";
    var text;
    if (jname.length < 5) {
        text = "Please Enter Valid Name:"
        jerror_message.innerHTML = text;
        return false;

    }
    if (jsubject.length <=10) {
        text = "Please Enter Subject Name:"
        jerror_message.innerHTML = text;
        return false;
    }
    if (isNaN(jphonenumber) || jphonenumber.length != 10) {
        text = "Please Enter your valid Phone Number";
        jerror_message.innerHTML = text;
        return false;
    }
    if (jmail.indexOf('@')==-1 || jmail.length<=6) {
        text = "Please Enter valid Email";
        jerror_message.innerHTML = text;  
        return false;
    }
    if (jmessage.length <=10) {
        text = "Please Enter more than 10 Charecters"
        jerror_message.innerHTML = text;
        return false;
    }
    alert("Form Submitted Successfully.");
    return true;

}