
        var game_table_html = " "
                    $.ajax({
                        type: 'GET',
                        url: 'http://localhost:8000/games/games_json/',
                        data: { get_param: 'value' },
                        dataType: 'json',
                        success: function (data) {
                                var json = data;

                        $.each(json,function (i,item){
                            game_table_html +=  "<li class='subitem1'><a href= " + json[i].game_name.toLowerCase() + ".html>" + json[i].game_name +"</a></li>"

                        });
                        $('#oyunlar').append(game_table_html)

                }
        });

