/**
 * Created by taha on 14.07.2017.
 */
//Adds a new game-which is added by the admin-to the navigation bar in the homepage

        // allows users to sign up to system if  they filled the necessary field.
        function validateForm(){
		    var name = document.forms["regForm"]["name"].value;
		    var surname = document.forms["regForm"]["surname"].value;
		    var username = document.forms["regForm"]["username"].value;
		    var email = document.forms["regForm"]["email"].value;
		    var password = document.forms["regForm"]["password"].value;

		    var re = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$";

		    if (username == "" && surname == "" && username == "" && email == "" && password == "" && re.test(password)){
		        alert("All of the fields must be filled and password should be Minimum eight characters, at least one letter and one number !!");
		        return false;
			}
		}