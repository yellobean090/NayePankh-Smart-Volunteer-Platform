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

document.addEventListener("DOMContentLoaded", () => {

    loadStats();

    loadVolunteers();

    loadAnalytics();

});


async function loadStats() {

    const response = await fetch("/stats");

    const data = await response.json();

    if (data.success) {

        document.getElementById("total-volunteers").textContent =
            data.total_volunteers;

        document.getElementById("active-volunteers").textContent =
            data.active_volunteers;

        document.getElementById("total-events").textContent =
            data.total_events;

        document.getElementById("monthly-registrations").textContent =
            data.registrations_this_month;
    }

}


async function loadVolunteers() {

    const response = await fetch("/volunteers");

    const data = await response.json();

    renderVolunteers(data.data);

}


function renderVolunteers(volunteers) {

    const tbody = document.getElementById(

        "volunteer-table-body"

    );

    tbody.innerHTML = "";

    volunteers.forEach(v => {

        tbody.innerHTML += `

            <tr>

                <td>${v.id}</td>

                <td>${v.name}</td>

                <td>${v.email}</td>

                <td>${v.city}</td>

                <td>${v.skills || "-"}</td>

                <td>${v.interests || "-"}</td>

            </tr>

        `;

    });

}


document.getElementById(

    "search-input"

).addEventListener(

    "input",

    searchVolunteers

);


document.getElementById(

    "skill-filter"

).addEventListener(

    "change",

    searchVolunteers

);


async function searchVolunteers() {

    const name = document.getElementById(

        "search-input"

    ).value;

    const skill = document.getElementById(

        "skill-filter"

    ).value;

    const response = await fetch(

        `/search-volunteers?name=${encodeURIComponent(name)}&skill=${encodeURIComponent(skill)}`

    );

    const data = await response.json();

    renderVolunteers(data.data);

}


document.getElementById(

    "export-btn"

).addEventListener(

    "click",

    () => {

        window.location.href =

            "/export-volunteers";

    }

);


async function loadAnalytics() {

    const response = await fetch(

        "/analytics"

    );

    const result = await response.json();

    const data = result.data;


    new Chart(

        document.getElementById(

            "volunteerChart"

        ),

        {

            type: "line",

            data: {

                labels:

                    data.volunteer_growth.labels,

                datasets: [

                    {

                        label: "Volunteers",

                        data:

                            data.volunteer_growth.values

                    }

                ]

            }

        }

    );


    new Chart(

        document.getElementById(

            "eventChart"

        ),

        {

            type: "bar",

            data: {

                labels:

                    data.event_participation.labels,

                datasets: [

                    {

                        label: "Participants",

                        data:

                            data.event_participation.values

                    }

                ]

            }

        }

    );


    new Chart(

        document.getElementById(

            "registrationChart"

        ),

        {

            type: "line",

            data: {

                labels:

                    data.monthly_registrations.labels,

                datasets: [

                    {

                        label: "Registrations",

                        data:

                            data.monthly_registrations.values

                    }

                ]

            }

        }

    );


    new Chart(

        document.getElementById(

            "skillChart"

        ),

        {

            type: "pie",

            data: {

                labels:

                    data.skill_distribution.labels,

                datasets: [

                    {

                        data:

                            data.skill_distribution.values

                    }

                ]

            }

        }

    );

}