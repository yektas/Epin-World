var game_table_html = " "
                    $.ajax({
                        type: 'GET',
                        url: 'http://localhost:8000/games/games_json/',
                        data: { get_param: 'value' },
                        dataType: 'json',
                        success: function (data) {
                                var json = data;

                              
                        $.each(json,function(i,item){
                            game_table_html +=  "<tr><td>" + json[i].game_name +"</td><td>"+ json[i].game_money_price + "</td></tr>"
                        
                        });
                        $('#games').append(game_table_html)                        
                        
                }
        });
