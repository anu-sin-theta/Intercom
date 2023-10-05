
const authenticationForm = document.getElementById("authenticationForm");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const loginButton = document.getElementById("loginButton");

// Static credentials for authentication
const staticUsername = "Staff";
const staticPassword = "Wingss_-123";

// Add click event listener to the login button
loginButton.addEventListener("click", () => {
    const email = emailInput.value;
    const password = passwordInput.value;

    // Check if the entered credentials match the static credentials
    if (email === staticUsername && password === staticPassword) {
        // Authentication successful
        console.log("User authenticated.");

        // Automatically redirect to "intercom.html" after authentication
        window.location.href = "index2.html";
    } else {
        // Authentication failed
        console.error("Authentication failed. Invalid credentials.");
    }
});
