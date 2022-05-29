function validation() {

    var name = document.myform.user_name;
    var LastName = document.myform.user_lastname;
    var phoneNum = document.myform.user_phone;
    var EmailId = document.myform.user_email;
   

    if(name == "") {
        printError("nameErr", "Please enter your name");
    } else {
        var regex = /^[a-zA-Z\s]+$/;                
        if(regex.test(name) === false) {
            printError("nameErr", "Please enter a valid name");
        } else {
            printError("nameErr", "");
            nameErr = false;
        }
    }
  
    if(LastName.value.length >12 ){
        alert('Name must be greater than 6 charters');
        LastName.focus();
        return false;
    }
    if (LastName.value.length == '') {

        alert("Please Enter FullName");
  
        return false;

    }
    if (isNaN(phoneNum.value)) {

        alert("your phone number must be Numeric Value only");

        return false;
    }
    if (isNaN(phoneNum.value)) {

        alert("your phone number must be Numeric Value only");

        return false;
    }

    if (phoneNum.value.length != 10) {

        alert("your phone number must be 10 Number only ");
        
        return false;
        
    }
    if (phoneNum.value.length <= 0) {

        alert("Please Enter Phone number");

        return false;
    }
    

    
    
}