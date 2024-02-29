function calculateTotal() {
    // Get the quantity of oranges and apples from input fields
    var orangeQuantity = parseInt(document.getElementById("orangeQuantity").value);
    var appleQuantity = parseInt(document.getElementById("appleQuantity").value);

    // Validate input: Ensure quantities are positive integers
    if (isNaN(orangeQuantity) || isNaN(appleQuantity) || orangeQuantity < 0 || appleQuantity < 0) {
        alert("Please enter a valid quantity for each product.");
        return;
    }

    // Calculate the total price
    var total = (orangeQuantity * 1.00) + (appleQuantity * 1.50);

    // Display the total price
    alert("Total Price: $" + total.toFixed(2));

    // Display summary of items added to the cart
    var summary = "Items added to cart:\n";
    if (orangeQuantity > 0) {
        summary += "Pixie Oranges: " + orangeQuantity + " piece(s)\n";
    }
    if (appleQuantity > 0) {
        summary += "Pixie Apples: " + appleQuantity + " piece(s)\n";
    }
    alert(summary);
}

function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    // Validate form fields
    if (name.trim() === '' || email.trim() === '' || message.trim() === '') {
        alert("Please fill in all fields.");
        return;
    }

    // Display submitted values
    alert("Thank you, " + name + "! Your message has been submitted:\n\nEmail: " + email + "\nMessage: " + message);
    // You can add further processing such as sending the form data to a backend server here
}

// Add event listener for form submission
document.getElementById("contactForm").addEventListener("submit", handleFormSubmit);
