function validation() {

    var Name=document.myform1.agency_name;
    var Address=document.myform1.address;
    var phoneNum = document.myform1.phone;
    var EmailId = document.myform1.email;
    var agency_file = document.myform1.agency_photo;
    var Iata_certificate = document.myform1.iata_certificate;
    
    if (EmailId.value.length <= 0) {

        alert("Please Enter Email Id");

        return false;
    }
    if (agency_file.value.length == " ") {
        alert("You forgot to attach Resume!");
        user_file.focus();
        return false;
    }
    if (Iata_certificate.value.length == " ") {
        alert("You forgot to attach Resume!");
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