from flask import Flask, render_template, request, jsonify
from database import get_connection
from ai.agent import recommend_opportunities
app = Flask(__name__)


# ==========================
# WEBSITE ROUTES
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ==========================
# VOLUNTEER APIs
# ==========================

@app.route("/register", methods=["POST"])
def register_volunteer():

    try:

        data = request.get_json()

        required_fields = [
            "name",
            "email",
            "phone",
            "city"
        ]

        for field in required_fields:

            if not data.get(field):

                return jsonify({
                    "success": False,
                    "message": f"{field} is required."
                }), 400

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO volunteers (

                name,
                email,
                phone,
                city,
                skills,
                interests,
                availability

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

        """, (

            data.get("name"),
            data.get("email"),
            data.get("phone"),
            data.get("city"),
            data.get("skills"),
            data.get("interests"),
            data.get("availability")

        ))

        connection.commit()

        connection.close()

        return jsonify({

            "success": True,
            "message": "Volunteer registered successfully."

        }), 201

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500


@app.route("/volunteers", methods=["GET"])
def get_volunteers():

    try:

        connection = get_connection()

        volunteers = connection.execute("""

            SELECT * FROM volunteers
            ORDER BY registration_date DESC

        """).fetchall()

        connection.close()

        volunteer_list = []

        for volunteer in volunteers:

            volunteer_list.append(dict(volunteer))

        return jsonify({

            "success": True,
            "count": len(volunteer_list),
            "data": volunteer_list

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500


@app.route("/volunteer/<int:volunteer_id>", methods=["DELETE"])
def delete_volunteer(volunteer_id):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            DELETE FROM volunteers
            WHERE id = ?

        """, (volunteer_id,))

        connection.commit()

        deleted_rows = cursor.rowcount

        connection.close()

        if deleted_rows == 0:

            return jsonify({

                "success": False,
                "message": "Volunteer not found."

            }), 404

        return jsonify({

            "success": True,
            "message": "Volunteer deleted successfully."

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500


# ==========================
# RUN APP
# ==========================


@app.route("/events-api", methods=["GET"])
def get_events():

    try:

        connection = get_connection()

        events = connection.execute("""

            SELECT * FROM events
            ORDER BY date ASC

        """).fetchall()

        connection.close()

        event_list = []

        for event in events:

            event_list.append(dict(event))

        return jsonify({

            "success": True,
            "count": len(event_list),
            "data": event_list

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500
    
@app.route("/event-register", methods=["POST"])
def register_for_event():

    try:

        data = request.get_json()

        volunteer_id = data.get("volunteer_id")

        event_id = data.get("event_id")

        if not volunteer_id or not event_id:

            return jsonify({

                "success": False,
                "message": "volunteer_id and event_id are required."

            }), 400

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""

            INSERT INTO event_registrations (

                volunteer_id,
                event_id

            )

            VALUES (?, ?)

        """, (

            volunteer_id,
            event_id

        ))

        connection.commit()

        connection.close()

        return jsonify({

            "success": True,
            "message": "Event registration successful."

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500

@app.route("/stats", methods=["GET"])
def get_stats():

    try:

        connection = get_connection()

        total_volunteers = connection.execute("""

            SELECT COUNT(*)
            FROM volunteers

        """).fetchone()[0]

        total_events = connection.execute("""

            SELECT COUNT(*)
            FROM events

        """).fetchone()[0]

        registrations_this_month = connection.execute("""

            SELECT COUNT(*)
            FROM volunteers

            WHERE strftime('%Y-%m', registration_date)
            =
            strftime('%Y-%m', 'now')

        """).fetchone()[0]

        active_volunteers = connection.execute("""

            SELECT COUNT(DISTINCT volunteer_id)
            FROM event_registrations

        """).fetchone()[0]

        connection.close()

        return jsonify({

            "success": True,

            "total_volunteers": total_volunteers,

            "active_volunteers": active_volunteers,

            "total_events": total_events,

            "registrations_this_month": registrations_this_month

        })

    except Exception as e:

        return jsonify({

            "success": False,
            "message": str(e)

        }), 500

@app.route("/recommend", methods=["POST"])
def recommend():

    try:

        data = request.get_json()

        interests = data.get("interests", "")

        availability = data.get("availability", "")

        recommendations = recommend_opportunities(

            interests,
            availability

        )

        return jsonify({

            "success": True,

            "recommendations": recommendations

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500

if __name__ == "__main__":

    print("NayePankh Backend Running Successfully!")

    app.run(debug=True)