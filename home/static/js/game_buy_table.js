/**
 * Created by taha on 18.07.2017.
 */
var game_table_item = ' '
           $.ajax({
                type: 'GET',
                url: 'http://localhost:8000/games/games_json/',
                data: { get_param: 'value' },
                    dataType: 'json',
                    success: function (data) {
                        var json = data;
                        $.each(json, function (i, item) {
                            game_table_item += "<div class='col-md-4 chain-grid'>" +"<a href='/users/game_detail/"+json[i].game_name+ "'/'"+">"+"+" +
                                "<img class='img-responsive chain' src="+ json[i].game_image_url +"alt=' ' /></a>" + "+" +
                                "<span class='star'> </span> <div class='grid-chain-bottom'> <h6>+" +
                                "<a href= "+ "/users/game_detail/Diablo3/" +json[i].game_name+"></a>"+ json[i].game_name +"</h6>" +
                                "<div class='star-price'> <div class='dolor-grid'>" +"<span class='actual'>" +json[i].game_money_price+"</span>" +"+" +
                                "</div>"+"</div>" +"<div class='clearfix'> </div> </div> </div> </div>"

                        });
                    }
});
function CreateTableFromJSON() {
        var col = [];
        for (var i = 0; i < game_table_item.length; i++) {
            for (var key in game_table_item[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }

        // CREATE DYNAMIC TABLE.
        var tableHTML = window.localStorage["sharedTable"];
        var table = document.createElement('table');
        table.innerHTML = tableHTML;

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        var tr = table.insertRow(-1);                   // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < game_table_item.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = game_table_item[i][col[j]];
            }
        }

        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        var divContainer = document.getElementById("showData");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    }