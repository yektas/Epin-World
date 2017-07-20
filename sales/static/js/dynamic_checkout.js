/**
 * Created by sercan on 21.07.2017.
 */
/**
 * Created by sercan on 19.07.2017.
 */

var productJSON = {
    "name": "Fifa2017",
    "price": "180",
    "company": "EA Sports"
};

var productName = document.getElementById("pname");
var companyName = document.getElementById("cname");
var price = document.getElementById("price");
var total = document.getElementById("total");


productName.textContent = productJSON.name;
companyName.textContent = productJSON.company;
price.textContent = productJSON.price;
total.textContent = price.textContent;
var cost = price.textContent;
var newPrice = 0;
var count;

$('#quantity').bind('keyup mousedown', function () {
    var quantity = document.getElementById("quantity");
    count = quantity.value;
    newPrice = count * cost;
    total.textContent = newPrice;
});