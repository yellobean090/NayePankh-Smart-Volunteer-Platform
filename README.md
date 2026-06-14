# NayePankh Smart Volunteer Management Platform

## Overview

NayePankh Smart Volunteer Management Platform is a production-inspired NGO management system designed to streamline volunteer engagement, event coordination, analytics, and AI-assisted support.

The platform was developed as an internship-ready project to demonstrate skills across Full-Stack Development, Backend Engineering, Python Development, AI Integration, Data Analytics, and UI/UX Design.

---

## Problem Statement

Non-Governmental Organizations (NGOs) often struggle with fragmented volunteer records, manual event coordination, limited reporting capabilities, and lack of intelligent support systems.

NayePankh Foundation required a centralized platform to:

* Manage volunteer registrations efficiently.
* Organize and promote community events.
* Track participation and organizational growth.
* Provide volunteers with instant assistance.
* Generate actionable insights through analytics.

---

## Proposed Solution

The NayePankh Smart Volunteer Management Platform provides:

* A modern NGO website.
* Volunteer registration and management.
* Event discovery and registration.
* Administrative dashboards.
* Interactive analytics visualizations.
* AI-powered chatbot assistance.
* Volunteer recommendation capabilities.

---

## Features

### NGO Website

* Home page with impact statistics and campaigns.
* About page highlighting mission and vision.
* Contact page with inquiry form and social links.
* Fully responsive design.

### Volunteer Management

* Volunteer registration form.
* Volunteer database storage using SQLite.
* Volunteer search functionality.
* Skill-based volunteer filtering.
* CSV export for reporting.

### Event Management

* Upcoming event listings.
* Event registration APIs.
* Event participation tracking.

### Admin Dashboard

* Total volunteers.
* Active volunteers.
* Total events.
* Monthly registrations.
* Volunteer management tools.

### Analytics Dashboard

* Volunteer Growth Trends.
* Event Participation Analysis.
* Monthly Registration Metrics.
* Skill Distribution Insights.

### AI Assistant

* Answers frequently asked questions.
* Explains volunteering procedures.
* Provides information about NayePankh Foundation.
* Gemini integration with fallback support.

### AI Volunteer Agent

* Accepts volunteer interests.
* Matches suitable opportunities.
* Generates personalized recommendations.

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js
* Font Awesome

### Backend

* Python
* Flask

### Database

* SQLite

### AI

* Google Gemini API
* Rule-based fallback assistant

### Deployment

* GitHub
* Render

---

## Project Structure

NayePankh-Smart-Volunteer-Platform/

backend/

├── app.py

├── database.py

├── requirements.txt

├── ai/

│ ├── chatbot.py

│ └── volunteer_agent.py

├── templates/

├── static/

│ ├── css/

│ └── js/

└── nayepankh.db

README.md

---

## API Documentation

### Volunteer APIs

POST /register

Registers a volunteer.

GET /volunteers

Returns all volunteers.

DELETE /volunteer/<id>

Deletes a volunteer.

GET /search-volunteers

Searches volunteers by name and skill.

GET /export-volunteers

Downloads volunteer data as CSV.

---

### Event APIs

GET /events-api

Returns event information.

POST /event-register

Registers volunteers for events.

---

### Dashboard APIs

GET /stats

Returns dashboard KPIs.

GET /analytics

Returns analytics datasets.

---

### AI APIs

POST /chat

Processes chatbot queries.

---

## Installation Guide

Clone the repository:

git clone <repository-url>

Navigate to backend:

cd backend

Create virtual environment:

python3 -m venv venv

Activate environment:

Linux/Mac:

source venv/bin/activate

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open:

http://127.0.0.1:5000

---

## Screenshots

Add screenshots for:

* Home Page
* Volunteer Registration
* Events Page
* Dashboard
* Analytics Charts
* AI Assistant

---

## Future Improvements

* Email notifications.
* Admin authentication.
* Volunteer attendance tracking.
* Real-time chatbot memory.
* Cloud database migration.
* Progressive Web App support.

---

## Learning Outcomes

Through this project, the following competencies were demonstrated:

* Full-stack web development.
* REST API development.
* Database design and integration.
* Data visualization techniques.
* AI application integration.
* UI/UX principles.
* Software deployment workflows.

---

## Conclusion

The NayePankh Smart Volunteer Management Platform demonstrates how technology can enhance the efficiency and impact of social organizations. The project combines modern web technologies, analytics, and artificial intelligence to create a scalable solution for NGO operations.
.
