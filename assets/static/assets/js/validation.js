function validation() {

    var Name=document.myform.name;
    var phoneNum = document.myform.contact;
    var EmailId = document.myform.email;
    var pass1 = document.myform.password;
    var pass2 = document.myform.confirm;
    var user_file = document.myform.image;
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;


   
    
    if(Name.value.length >12 ){
        alert('Name must be greater than 6 charters');
        Name.focus();
        return false;
    }
    if (Name.value.length == '') {

        alert("Please Enter FullName");
  
        return false;

    }
    if (isNaN(phoneNum.value)) {

        alert("Enter Numeric Value only");

        return false;
    }
    if (phoneNum.value.length != 10) {

        alert("please Enter valid ");
        
        return false;
        
    }
    if (phoneNum.value.length <= 0) {

        alert("Please Enter Email Id");

        return false;
    }
    if (user_file.value.length == " ") {
        alert("You forgot to attach Resume!");
        user_file.focus();
        return false;
    }

    if (EmailId.value.length <= 0) {

        alert("Please Enter Email Id");

        return false;
    }
    

     
   
    
    
}