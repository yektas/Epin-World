

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});
alert("asd")

var game_product_footer = ""

$.ajax({

                type: 'GET',
                url: 'http://localhost:8000/games/games_json/',
                data: { get_param: 'value' },
                    dataType: 'json',
                    success: function (data) {
                            var json = data;


                    $.each(json,function(i,item){
                        if(i<=3){
                          /*
                            game_product_footer +=  "<div class='col-sm-3'> <article class='col-item'> <div class='photo'> <div class='options-cart'>" +" <a href='/users/game_detail/" +json[i].game_name+"> <button class='btn btn-default' title='Add to cart'> <span class='fa fa-shopping-cart'></span> </button> </a></div>"
                            game_product_footer += "<a href=''> <img src='{% static 'images/json[i].game_name+.jpg'%}' class='img-responsive' alt='Product Image' /> </a>"
                            game_product_footer += "</div><div class='container'><br> <strong><p>"+json[i].game_name+"</p></strong>"
                            game_product_footer += " <strong><p>"+json[i].game_money_price+"</p></strong>"
                            game_product_footer += "  </div></article></div>"
                          */
                        }

                     });
                     $('#products_footer').append(game_product_footer)

                }
});








