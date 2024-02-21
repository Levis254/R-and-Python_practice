function calculateTotal() {
    // Get the quantity of oranges and apples from input fields
    var orangeQuantity = parseInt(document.getElementById("orangeQuantity").value);
    var appleQuantity = parseInt(document.getElementById("appleQuantity").value);

    // Calculate the total price
    var total = (orangeQuantity * 1.00) + (appleQuantity * 1.50);

    // Display the total price
    alert("Total Price: $" + total.toFixed(2));
}
