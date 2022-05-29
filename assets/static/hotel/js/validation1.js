
function validation() {

    var Name=document.myform1.hotel_name;
    var Address=document.myform1.address;
    var phoneNum = document.myform1.phone;
    var EmailId = document.myform1.email;
    var user_file = document.myform1.hotel_photo;
    var user_certificate = document.myform1.hotel_certificate;
    
    if (EmailId.value.length <= 0) {

        alert("Please Enter Email Id");

        return false;
    }
    if (user_file.value.length == " ") {
        alert("You forgot to attach images!");
        user_file.focus();
        return false;
    }
    if (user_certificate.value.length == " ") {
        alert("You forgot to attach images!");
        user_file.focus();
        return false;
    }
 
    

    
    if(Name.value.length >12 ){
        alert('Name must be greater than 6 charters');
        Name.focus();
        return false;
    }
   
    if (Name.value.length == '') {

        alert("Please Enter FullName");
  
        return false;

    }
    
    
  
    if(Address.value.length >12 ){
        alert('Name must be greater than 6 charters');
        LastName.focus();
        return false;
    }
    if (Address.value.length == '') {

        alert("Please Enter FullName");
  
        return false;

    }
    if (isNaN(phoneNum.value)) {

        alert("Enter Numeric Value only");

        return false;
    }
    if (isNaN(phoneNum.value)) {

        alert("Enter Numeric Value only");

        return false;
    }

    if (phoneNum.value.length != 10) {

        alert("please Enter valid phone num ");
        
        return false;
        
    }
    if (phoneNum.value.length <= 0) {

        alert("Please Enter Phone number");

        return false;
    }
    

    
    
}