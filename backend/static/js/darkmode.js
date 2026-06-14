const toggleButton = document.getElementById("dark-mode-toggle");

const body = document.body;


if (localStorage.getItem("theme") === "dark") {

    body.classList.add("dark-mode");

    if (toggleButton) {

        toggleButton.innerHTML =
            '<i class="fa-solid fa-sun"></i>';

    }

}


if (toggleButton) {

    toggleButton.addEventListener("click", () => {

        body.classList.toggle("dark-mode");


        if (body.classList.contains("dark-mode")) {

            localStorage.setItem("theme", "dark");

            toggleButton.innerHTML =
                '<i class="fa-solid fa-sun"></i>';

        }

        else {

            localStorage.setItem("theme", "light");

            toggleButton.innerHTML =
                '<i class="fa-solid fa-moon"></i>';

        }

    });

}