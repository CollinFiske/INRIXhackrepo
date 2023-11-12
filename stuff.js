function getValue() {
    // Get the value from the input field
  var from = document.getElementById("from").value;
  var to = document.getElementById("to").value;
  var mileage = document.getElementById("mileage").value;

    // Now 'userInput' contains the value entered by the user
    // You can perform actions or logic with this variable
  console.log("From: ", from);
  console.log("To: ", to);
  console.log("Mileage:", mileage);
}
