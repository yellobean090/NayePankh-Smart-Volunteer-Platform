document.addEventListener("DOMContentLoaded", () => {

    const toggleButton = document.getElementById("chat-toggle");

    const chatbotContainer = document.getElementById("chatbot-container");

    const closeButton = document.getElementById("chat-close");

    const sendButton = document.getElementById("chat-send");

    const inputField = document.getElementById("chat-input");

    const messagesContainer = document.getElementById("chat-messages");


    function addMessage(message, sender) {

        const div = document.createElement("div");

        div.classList.add("chat-message");

        div.classList.add(sender);

        div.textContent = message;

        messagesContainer.appendChild(div);

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }


    async function sendMessage() {

        const message = inputField.value.trim();

        if (!message) return;

        addMessage(message, "user");

        inputField.value = "";

        addMessage("Typing...", "bot");

        try {

            const response = await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    message: message

                })

            });

            const data = await response.json();

            messagesContainer.lastChild.remove();

            addMessage(

                data.response,

                "bot"

            );

        }

        catch (error) {

            messagesContainer.lastChild.remove();

            addMessage(

                "Sorry, something went wrong.",

                "bot"

            );

        }

    }


    toggleButton.addEventListener("click", () => {

        chatbotContainer.classList.toggle("show-chat");

    });


    closeButton.addEventListener("click", () => {

        chatbotContainer.classList.remove("show-chat");

    });


    sendButton.addEventListener("click", sendMessage);


    inputField.addEventListener("keypress", (e) => {

        if (e.key === "Enter") {

            sendMessage();

        }

    });

});