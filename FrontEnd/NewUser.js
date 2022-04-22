function checkPasswordMatch () {

    var pass1 = document.getElementById('password1').value;
    var pass2 = document.getElementById('password2').value;

    if (pass1 != pass2) {
        
        alert("passwords do not match");

        return false;
    }

    return true;
}