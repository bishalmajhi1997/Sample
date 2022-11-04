function Register() {
    var jname = document.form1.name.value;
    var jemail = document.form1.email.value;
    var jpassword = document.form1.password.value;
    var jmobile = document.form1.contact.value;
    var jcity = document.form1.city;
    var jcommits = document.form1.commits.value;
    console.log(jname);
    if (jname=="") {
        window.alert("Please enter your name:");
        return false;
    }
    if (jemail=="") {
        window.alert("Please enter your email:");
        return false;

    }
    if (jpassword == "") {
        window.alert("Please enter your password:");
        return false;

    }
    if (jmobile == "") {
        window.alert("Please enter your contact details:");
        return false;


    }
    if (jcity.selectIndex < 0) {
        window.alert("Please enter your city:");
        return false;

    }
    if (jcommits == "") {
        window.alert("Please enter your commits");
        return false;
    }
    alert("form submitted successfully");
    return true;

}