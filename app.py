from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "")
    email = request.form.get("email", "")

    message = (
        "New Website Submission\n"
        f"Name: {name}\n"
        f"Email: {email}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={"chat_id": CHAT_ID, "text": message},
        timeout=15
    )

    if response.ok:
        return "Message sent to Telegram successfully!"

    return "Telegram message failed. Check your bot settings.", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
