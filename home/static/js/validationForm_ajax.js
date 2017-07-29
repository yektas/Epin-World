/**
 * Created by taha on 14.07.2017.
 */
//Adds a new game-which is added by the admin-to the navigation bar in the homepage

        // allows users to sign up to system if  they filled the necessary field.
        function validateForm(){
		    var name = document.forms["user-form"]["name"].value;
		    var surname = document.forms["user-form"]["surname"].value;
		    var username = document.forms["user-form"]["username"].value;
		    var email = document.forms["user-form"]["email"].value;
		    var password = document.forms["user-form"]["password"].value;
		    var re = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$";
		    alert(password);

		    if (re.test(password)){
		        alert("All of the fields must be filled and password should be Minimum eight characters, at least one letter and one number !!");
		        return false;
			}
		}