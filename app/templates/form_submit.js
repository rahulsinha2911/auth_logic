document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registerForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(form);
        const jsonData = {};

        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        fetch("/auth/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(jsonData),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Success:", data);
            // Handle success - you might want to redirect or show a message
        })
        .catch((error) => {
            console.error("Error:", error);
            // Handle error - display error message to the user
        });
    });
});
