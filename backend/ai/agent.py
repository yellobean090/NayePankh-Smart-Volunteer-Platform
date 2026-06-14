def recommend_opportunities(interests, availability=""):

    interests = interests.lower()

    recommendations = []

    if "education" in interests or "teaching" in interests:
        recommendations.extend([
            "Education Support Drive",
            "Student Mentorship Program",
            "Weekend Literacy Initiative"
        ])

    if "environment" in interests or "green" in interests:
        recommendations.extend([
            "Tree Plantation Campaign",
            "Community Clean-Up Drive"
        ])

    if "health" in interests or "medical" in interests:
        recommendations.extend([
            "Health Awareness Camp",
            "Rural Healthcare Outreach"
        ])

    if "design" in interests:
        recommendations.extend([
            "Social Media Awareness Campaign",
            "NGO Branding Support"
        ])

    if "technology" in interests or "coding" in interests:
        recommendations.extend([
            "Digital Literacy Workshops",
            "NGO Website Development Team"
        ])

    if availability.lower() == "weekends":
        recommendations.append(
            "Weekend Community Engagement Program"
        )

    if len(recommendations) == 0:
        recommendations = [
            "General Volunteer Orientation",
            "Community Support Initiatives"
        ]

    return list(set(recommendations))