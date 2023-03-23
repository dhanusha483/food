from flask import Flask, request, render_template
import openai
import os

# Set up Flask app and OpenAI API key
app = Flask(_name_)
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define route for chat messages
@app.route("/chat", methods=["POST"])
def chat():
    # Get message from user
    message = request.form["message"]
    # Send message to ChatGPT and retrieve response
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.7,
    ).choices[0].text.strip()
    # Render response as a message in the chat interface
    return {"message": response}

# Define route for chat interface
@app.route("/")
def index():
    return render_template("chat.html")

if _name_ == "_main_":
    app.run()