document.addEventListener("DOMContentLoaded", () => {

    const volunteerForm = document.getElementById("volunteer-form");

    if (!volunteerForm) {
        return;
    }

    volunteerForm.addEventListener("submit", async (event) => {

        event.preventDefault();

        const submitButton = volunteerForm.querySelector(
            'button[type="submit"]'
        );

        submitButton.disabled = true;
        submitButton.textContent = "Registering...";

        const volunteerData = {

            name: document.getElementById("name").value.trim(),

            email: document.getElementById("email").value.trim(),

            phone: document.getElementById("phone").value.trim(),

            city: document.getElementById("city").value.trim(),

            skills: document.getElementById("skills").value.trim(),

            interests: document.getElementById("interests").value.trim(),

            availability: document.getElementById("availability").value.trim()

        };

        try {

            const response = await fetch("/register", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(volunteerData)

            });

            const result = await response.json();

            if (result.success) {

                alert(result.message);

                volunteerForm.reset();

            } else {

                alert(result.message || "Registration failed.");

            }

        } catch (error) {

            console.error(error);

            alert("Unable to connect to the server.");

        } finally {

            submitButton.disabled = false;
            submitButton.textContent = "Register Now";

        }

    });

});