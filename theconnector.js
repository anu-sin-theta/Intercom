const firebaseConfig = {
    apiKey: "AIzaSyA-V61Tw27Q-2NVfV7i_twZCA3K5N-P_uE",
    authDomain: "csed-intercom.firebaseapp.com",
    databaseURL: "https://csed-intercom-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "csed-intercom",
    storageBucket: "csed-intercom.appspot.com",
    messagingSenderId: "597649540949",
    appId: "1:597649540949:web:bfb74efa3e7eed00cf51dc",
    measurementId: "G-0FJGEY4K5S"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get a reference to the Firebase Realtime Database
const database = firebase.database();

// Add event listeners to buttons
const allowButton = document.getElementById("allowButton");
allowButton.addEventListener("click", () => {
    writeToDatabase("Allow");
});

const denyButton = document.getElementById("denyButton");
denyButton.addEventListener("click", () => {
    writeToDatabase("Deny");
});

const viewButton = document.getElementById("viewButton");
viewButton.addEventListener("click", () => {
    writeToDatabase("View");
});

// Function to write data to the Firebase Realtime Database
function writeToDatabase(value) {
    // Write the value to the database
    database.ref("buttonValue").set(value)
        .then(() => {
            console.log("Data written to the database successfully.");
            showSuccessMessage();
        })
        .catch((error) => {
            console.error("Error writing data to the database:", error);
        });
}

// Function to read data from the Firebase Realtime Database
function readFromDatabase() {
    // Read the value from the database
    database.ref("buttonValue").once("value")
        .then((snapshot) => {
            const value = snapshot.val();
            console.log("Value from the database:", value);
        })
        .catch((error) => {
            console.error("Error reading data from the database:", error);
        });
}

// Function to show a success message
function showSuccessMessage() {
    const successMessage = document.createElement("div");
    successMessage.className = "success";
    successMessage.textContent = "Data written to the database successfully!";
    document.body.appendChild(successMessage);

    // Remove the success message after a few seconds
    setTimeout(() => {
        successMessage.remove();
    }, 3000); // Remove after 3 seconds
}
