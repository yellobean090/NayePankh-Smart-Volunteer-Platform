document.addEventListener("DOMContentLoaded", async () => {

    try {

        const response = await fetch("/analytics");

        const result = await response.json();

        if (!result.success) {

            console.error("Analytics fetch failed.");

            return;
        }

        const data = result.data;


        // Volunteer Growth

        new Chart(document.getElementById("volunteerChart"), {

            type: "line",

            data: {

                labels: data.volunteer_growth.labels,

                datasets: [{

                    label: "Volunteers",

                    data: data.volunteer_growth.values,

                    tension: 0.4

                }]
            }
        });


        // Event Participation

        new Chart(document.getElementById("eventChart"), {

            type: "bar",

            data: {

                labels: data.event_participation.labels,

                datasets: [{

                    label: "Participants",

                    data: data.event_participation.values

                }]
            }
        });


        // Monthly Registrations

        new Chart(document.getElementById("registrationChart"), {

            type: "line",

            data: {

                labels: data.monthly_registrations.labels,

                datasets: [{

                    label: "Registrations",

                    data: data.monthly_registrations.values,

                    tension: 0.4

                }]
            }
        });


        // Skill Distribution

        new Chart(document.getElementById("skillChart"), {

            type: "pie",

            data: {

                labels: data.skill_distribution.labels,

                datasets: [{

                    data: data.skill_distribution.values

                }]
            }
        });

    }

    catch (error) {

        console.error(

            "Analytics Error:",

            error

        );
    }

});