import os
from dotenv import load_dotenv
from google import genai


# =====================================
# LOAD ENVIRONMENT VARIABLES
# =====================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# =====================================
# INITIALIZE GEMINI CLIENT
# =====================================

client = None

if GEMINI_API_KEY:

    try:

        client = genai.Client(

            api_key=GEMINI_API_KEY

        )

        print("Gemini client initialized successfully.")

    except Exception as e:

        print(

            f"Gemini initialization failed: {e}"

        )


# =====================================
# CONVERSATION MEMORY
# =====================================

conversation_history = []


# =====================================
# SYSTEM PROMPT
# =====================================

SYSTEM_PROMPT = """
You are NayePankh AI Assistant.

Your purpose is to assist users regarding
NayePankh Foundation.

Foundation Mission:

NayePankh Foundation empowers underprivileged
communities through education, healthcare,
environmental initiatives, awareness campaigns,
and volunteer-driven social impact programs.

Responsibilities:

1. Explain NayePankh's mission and initiatives.

2. Guide users on how to become volunteers.

3. Explain the volunteer registration process.

4. Explain how users can support the foundation.

5. Answer FAQs related to campaigns and events.

6. Encourage community participation.

Guidelines:

- Be professional and friendly.
- Keep answers concise and practical.
- Focus only on NayePankh-related topics.
- If unsure, advise users to contact the foundation.
- Never generate harmful content.
"""


# =====================================
# FAQ FALLBACK RESPONSES
# =====================================

FAQ_RESPONSES = {

    "volunteer":

        "You can volunteer with NayePankh Foundation "
        "by completing the registration form on the "
        "Volunteer page. Our team reviews applications "
        "and connects volunteers with suitable programs.",


    "donate":

        "You can support NayePankh Foundation through "
        "donations, fundraising initiatives, or by "
        "contributing your skills and time to community "
        "projects.",


    "mission":

        "NayePankh Foundation aims to empower "
        "underprivileged communities through education, "
        "healthcare support, environmental campaigns, "
        "and volunteer-driven social initiatives.",


    "events":

        "Visit the Events page to explore upcoming "
        "campaigns, awareness programs, and community "
        "engagement opportunities.",


    "contact":

        "You can reach NayePankh Foundation through the "
        "Contact page available on this platform.",


    "registration":

        "Volunteer registration requires basic details "
        "such as your name, email, phone number, city, "
        "skills, interests, and availability."
}


# =====================================
# GEMINI CHATBOT FUNCTION
# =====================================

def get_chatbot_response(user_message):

    try:

        conversation_history.append(

            f"User: {user_message}"

        )

        conversation_context = "\n".join(

            conversation_history[-10:]

        )

        prompt = f"""

{SYSTEM_PROMPT}

Conversation History:

{conversation_context}

Assistant:

"""

        if client:

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=prompt

            )

            assistant_reply = response.text

            conversation_history.append(

                f"Assistant: {assistant_reply}"

            )

            return {

                "success": True,

                "source": "gemini",

                "response": assistant_reply

            }

    except Exception as e:

        print(

            f"Gemini Error: {e}"

        )

    # =====================================
    # FALLBACK CHATBOT
    # =====================================

    message = user_message.lower()

    for keyword, answer in FAQ_RESPONSES.items():

        if keyword in message:

            conversation_history.append(

                f"Assistant: {answer}"

            )

            return {

                "success": True,

                "source": "fallback",

                "response": answer

            }

    default_response = (

        "Thank you for reaching out to NayePankh "
        "Foundation. Please explore our website or "
        "contact our team for detailed assistance "
        "regarding volunteering, events, or support "
        "opportunities."

    )

    conversation_history.append(

        f"Assistant: {default_response}"

    )

    return {

        "success": True,

        "source": "fallback",

        "response": default_response

    }


# =====================================
# CLEAR CHAT MEMORY
# =====================================

def clear_chat_history():

    conversation_history.clear()    