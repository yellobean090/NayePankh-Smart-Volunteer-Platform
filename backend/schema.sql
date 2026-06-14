DROP TABLE IF EXISTS volunteers;

CREATE TABLE volunteers (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    phone TEXT NOT NULL,

    city TEXT NOT NULL,

    skills TEXT,

    interests TEXT,

    availability TEXT,

    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



DROP TABLE IF EXISTS events;

CREATE TABLE events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    description TEXT NOT NULL,

    date TEXT NOT NULL,

    location TEXT NOT NULL

);



DROP TABLE IF EXISTS event_registrations;

CREATE TABLE event_registrations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    volunteer_id INTEGER NOT NULL,

    event_id INTEGER NOT NULL,

    FOREIGN KEY (volunteer_id) REFERENCES volunteers(id),

    FOREIGN KEY (event_id) REFERENCES events(id)

);