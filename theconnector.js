const firebaseConfig = {
    apiKey: "AIzaSyA-V61Tw27Q-2NVfV7i_twZCA3K5N-P_uE",
    authDomain: "csed-intercom.firebaseapp.com",
    databaseURL: "https://csed-intercom.asia-southeast1.firebasedatabase.app",
    projectId: "csed-intercom",
    storageBucket: "csed-intercom.appspot.com",
    messagingSenderId: "597649540949",
    appId: "1:597649540949:web:bfb74efa3e7eed00cf51dc",
    measurementId: "G-0FJGEY4K5S"
};
//dekh bhai inspect karne se kuch nahi hoga tumhe isme se kuch nahi milega source code dekhna hai toh github pe jao @anu-sin-theta.
//all credential are locked in firebase so you can't access it. reCAPTCHA is also locked so you can't access it.
firebase.initializeApp(firebaseConfig);

const database = firebase.database();

const allowButton = document.getElementById("allowButton");
allowButton.addEventListener("click", () => {
    writeToDatabase("Allow");
        setTimeout(function () {
        removeData();
    }, 8000);
});

const denyButton = document.getElementById("denyButton");
denyButton.addEventListener("click", () => {
    writeToDatabase("Deny");
        setTimeout(function () {
        removeData();
    }, 8000);
});

const view = document.getElementById("view");
view.addEventListener("click", () => {
    writeToDatabase("View");
        setTimeout(function () {
        removeData();
    }, 4000);
});

const viewButton = document.getElementById("camera");
viewButton.addEventListener("change", () => {
    if (viewButton.checked) {
        writeToDatabase("Camera");
    }
    else {
        database.ref("Camera").remove();
    }
});


function writeToDatabase(value) {
    if (value === "View") {
        database.ref("viewButton").set("View")
            .then(() => {
                console.log("Data written to the database successfully.");
                showSuccessMessage();
            })
            .catch((error) => {
                console.error("Error writing data to the database:", error);
            });
    }
    if (value === "Allow") {
        database.ref("allowButton").set("Allow")
            .then(() => {
                console.log("Data written to the database successfully.");
                showSuccessMessage();
            })
            .catch((error) => {
                console.error("Error writing data to the database:", error);
            });
    }
    if (value === "Deny") {
        database.ref("denyButton").set("Deny")
            .then(() => {
                console.log("Data written to the database successfully.");
                showSuccessMessage();
            })
            .catch((error) => {
                console.error("Error writing data to the database:", error);
            });
    }
    setTimeout(function () {
        removeData();
    }, 8000);

    if (value === "Camera") {
        database.ref("cameraStatus").set("Camera")
            .then(() => {
                console.log("Data written to the database successfully.");
                showSuccessMessage();
            })
            .catch((error) => {
                console.error("Error writing data to the database:", error);
            });
    }
}
//function to allow and push notification


// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Function to read and display door status
    function readDoorStatus() {
        const doorStatusElement = document.getElementById("Status"); // Get the status element

        database.ref("doorStatus").on("value", (snapshot) => {
            const doorStatus = snapshot.val();
            console.log(doorStatus);
            if (doorStatus === "Open") {
                doorStatusElement.innerHTML = "Door is Open";
                doorStatusElement.style.color = "#4CAF50"; // Optional: Change text color for "Open"
            } else if (doorStatus === "Close") {
                doorStatusElement.innerHTML = "Door is Closed";
                doorStatusElement.style.color = "#f44336"; // Optional: Change text color for "Closed"
            } else {
                doorStatusElement.innerHTML = "Not updated, check R-pi's internet connection :)"; // Handle other status values if needed
                doorStatusElement.style.color = "#333333";
            }
        });
    }

    readDoorStatus();
});

function refreshPage() {
    location.reload();
}

const refreshButton = document.getElementById("refreshButton");
refreshButton.addEventListener("click", refreshPage);

function removeData() {
    database.ref("allowButton").remove()
    database.ref("denyButton").remove()
    database.ref("viewButton").remove()
    database.ref("cameraStatus").remove()
}




function showSuccessMessage() {
    const successMessage = document.createElement("div");
    successMessage.className = "success";
    successMessage.textContent = "Data written to the database successfully!";
    document.body.appendChild(successMessage);

    setTimeout(() => {
        successMessage.remove();
    }, 3000);
}
