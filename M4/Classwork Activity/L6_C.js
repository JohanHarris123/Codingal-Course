function validate(e) {
    e.preventDefault();
    //Prevents the default behavior of the form submission (which is to reload the page). This allows custom validation to occur before deciding whether to submit the form.

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgBox = document.getElementById("message");

    let message = "";
    if (email === "") {
        message = "Please enter an email.";
        msgBox.style.color = "red";
    } else if (password === "") {
        message = "Password must be at least 8 characters.";
        msgBox.style.color = "red";
    } else if (age === "") {
        message = "Please enter an age.";
        msgBox.style.color = "red";
    }
    else {
        message = "Login successful!";
        msgBox.style.color = "green";
    }

    msgBox.innerHTML = message;
    //Displays the message (error or success) inside the message box element.
}