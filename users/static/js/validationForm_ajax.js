/**
 * Created by taha on 14.07.2017.
 */
//Adds a new game-which is added by the admin-to the navigation bar in the homepage
var game_table_html = " "
var k = 0;
                    $.ajax({
                        type: 'GET',
                        url: 'http://localhost:8000/games/games_json/',
                        data: { get_param: 'value' },
                        dataType: 'json',
                        success: function (data) {
                                var json = data;

                        $.each(json,function (i,item){
                            game_table_html +=  "<li class='subitem1'><a href= " + json[i].game_name.toLowerCase() + ".html>" + json[i].game_name +"</a></li>"

                            k += 1
                            if(k==2){
                                
                            }

                        });

                        console.log("asdasd");
                        $('#oyunlar').append(game_table_html)
                }
        });
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