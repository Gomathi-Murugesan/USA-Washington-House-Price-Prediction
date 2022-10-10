
function onClickedEstimatePrice() {
    console.log('Estimate price clicked');
    var total_sqft = document.getElementById('uisqft');
    var bathrooms = document.getElementById('uibathrooms');
    var bedrooms = document.getElementById('uibedrooms');
    var city = document.getElementById('uicities');
    var year_built = document.getElementById('uiyear');
    var estimate_price = document.getElementById('uiEstimatedPrice');

    var url = "/app1/predict_house_price";

    $.post(url, {
        sqft_living : parseFloat(total_sqft.value),
        city : city.value,
        bathrooms : bathrooms.value,
        bedrooms : bedrooms.value,
        yr_built : year_built.value,
    }, function(data, status) {
        console.log(data.estimated_price);
        estimate_price.innerHTML = "<h2>" + data.estimated_price.toString() + " " + "Dollars</h2>";
        console.log(status);       
    });
}

function onloadCity() {
    console.log("document loaded");
    var url = "/app1/get_cities_name";
    $.get(url, function(data, status) {
        console.log("got response for get_cities_name request");
        if (data) {
            var cities = data.cities;
            var uicities = document.getElementById("uicities");
            $('#uicities').empty();
            for(var i in cities) {
                var next_city = new Option(cities[i]) 
                $('#uicities').append(next_city);
            }
        }
    });

}

window.onload = onloadCity;