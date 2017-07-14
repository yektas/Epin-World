
var game_table_html = " "
           $.ajax({

                type: 'GET',
                url: 'http://localhost:8000/games/games_json/',
                data: { get_param: 'value' },
                    dataType: 'json',
                    success: function (data) {
                            var json = data;


                    $.each(json,function(i,item){
                         game_table_html += "<div class='col-md-4 chain-grid'>" +"<a href='single.html'><img class='img-responsive chain' src="+ json[i].game_image_url +"alt=' ' /></a>" + "<span class='star'> </span> <div class='grid-chain-bottom'> <h6><a href='single.html'> " +json[i].game_money_price+"</a></h6>" +  "<div class='star-price'> <div class='dolor-grid'>" +"<span class='actual'>"+json[i].game_name+"</span>" +"	</div>"+"</div>" +"<div class='clearfix'> </div> </div> </div> </div>"



                     });
                     $('#game_index_table').append(game_table_html)

                }
});
