import sqlite3


DATABASE = "nayepankh.db"


def get_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    with open("schema.sql", "r") as file:

        connection.executescript(file.read())

    connection.commit()

    connection.close()

    print("Database initialized successfully!")

def seed_events():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")

    count = cursor.fetchone()[0]

    if count == 0:

        events = [

            (
                "Education Support Drive",
                "Mentor children and assist educational workshops.",
                "2026-07-25",
                "Lucknow"
            ),

            (
                "Tree Plantation Campaign",
                "Environmental sustainability initiative.",
                "2026-08-02",
                "Gomti Nagar"
            ),

            (
                "Health Awareness Camp",
                "Community healthcare awareness event.",
                "2026-08-15",
                "Lucknow"
            )

        ]

        cursor.executemany("""

            INSERT INTO events (

                title,
                description,
                date,
                location

            )

            VALUES (?, ?, ?, ?)

        """, events)

        connection.commit()

        print("Sample events added.")

    connection.close()