function edit_row(no) {
    document.getElementById("edit_button" + no).style.display = "none";
    document.getElementById("save_button" + no).style.display = "block";

    var car_type = document.getElementById("car_type_row" + no);
    var car_model = document.getElementById("car_model_row" + no);
    var car_no = document.getElementById("car_no_row" + no);
    var select_car = document.getElementById("select_car_row" + no);
    var price = document.getElementById("price_row" + no);

    var car_type_data = car_type.innerHTML;
    var car_model_data = car_model.innerHTML;
    var car_no_data = car_no.innerHTML;
    var select_car_data = select_car.innerHTML;
    var price_data = price.innerHTML;

    car_type.innerHTML = "<input type='text' id='car_type_text" + no + "' value='" + car_type_data + "'>";
    car_model.innerHTML = "<input type='text' id='car_model_text" + no + "' value='" + car_model_data + "'>";
    car_no.innerHTML = "<input type='text' id='car_no_text" + no + "' value='" + car_no_data + "'>";
    select_car.innerHTML = "<input type='text' id='select_car_text" + no + "' value='" + select_car_data + "'>";
    price.innerHTML = "<input type='text' id='price_text" + no + "' value='" + price_data + "'>";
}

function save_row(no) {
    var car_type_val = document.getElementById("car_type_text" + no).value;
    var car_model_val = document.getElementById("car_model_text" + no).value;
    var car_no_val = document.getElementById("car_no_text" + no).value;
    var select_car_val = document.getElementById("select_car_text" + no).value;
    var price_val = document.getElementById("price_text" + no).value;

    document.getElementById("car_type_row" + no).innerHTML = car_type_val;
    document.getElementById("car_model_row" + no).innerHTML = car_model_val;
    document.getElementById("car_no_row" + no).innerHTML = car_no_val;
    document.getElementById("select_car_row" + no).innerHTML = select_car_val;
    document.getElementById("price_row" + no).innerHTML = price_val;

    document.getElementById("edit_button" + no).style.display = "block";
    document.getElementById("save_button" + no).style.display = "none";
}

function delete_row(no) {
    document.getElementById("row" + no + "").outerHTML = "";
}

function add_row() {
    var new_car_type = document.getElementById("new_car_type").value;
    var new_car_model = document.getElementById("new_car_model").value;
    var new_car_no = document.getElementById("new_car_no").value;
    var new_select_car = document.getElementById("new_select_car").value;
    var new_price = document.getElementById("new_price").value;

    var table = document.getElementById("data_table");
    var table_len = (table.rows.length) - 1;
    var row = table.insertRow(table_len).outerHTML = "<tr id='row" + table_len + "'><td id='car_type_row" + table_len + "'>" + new_car_type + "</td><td id='car_model_row" + table_len + "'>" + new_car_model + "</td><td id='car_no_row" + table_len + "'>" + new_car_no + "</td><td id='select_car_row" + table_len + "'>" + new_select_car + "</td><td id='price_row" + table_len + "'>" + new_price + "</td><td><input type='button' id='edit_button" + table_len + "' value='Edit' class='edit' onclick='edit_row(" + table_len + ")'> <input type='button' id='save_button" + table_len + "' value='Save' class='save' onclick='save_row(" + table_len + ")'> <input type='button' value='Delete' class='delete' onclick='delete_row(" + table_len + ")'></td></tr>";

    document.getElementById("new_car_type").value = "";
    document.getElementById("new_car_model").value = "";
    document.getElementById("new_car_no").value = "";
    document.getElementById("new_select_car").value = "";
    document.getElementById("new_price").value = "";
}