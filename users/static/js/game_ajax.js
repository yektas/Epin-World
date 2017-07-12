var drop_down = ""
	$.ajax({
		type: 'GET',
		url: 'http://localhost:8000/games/games_json/'
		data: {get_param: value}
		dataType: 'json',
                        success: function (data) {
                                alert("OYUN EKLENDİ!");
                                var json = data;
                                obj = JSON.parse(json);


			                        $.each(obj,function(i,item){
			                        	var game_name = obj[i].game_name
			                            trHTML += "<li class = " +game_name.toLowerCase() + ">"+"<a href= ' "+ game_name.toLowerCase() +".html"+" '>"+ game_name.toUpperCase()+"</a></li>" ;
			 
			                        });
			                         $(".cute").append(drop_down);
			        
                               	}


	})