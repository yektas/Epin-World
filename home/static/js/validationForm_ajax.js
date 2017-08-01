/**
 * Created by taha on 14.07.2017.
 */
//Adds a new game-which is added by the admin-to the navigation bar in the homepage
// allows users to sign up to system if  they filled the necessary field.

function validateForm() {
    var str = $("input[name=password]").val();

    if (str.search(/\d/) == -1) {
        alert("You should enter a digit");
        return false;
    } else if (str.search(/[a-zA-Z]/) == -1) {
        alert("You should enter a letter");
        return false;
    } else if (str.search(/[^a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_\+\.\,\;\:]/) != -1) {
        alert("No special character should be entered");
        return false;
    }
    else {
        alert("Successfull registration...");
        return true;
    }
}