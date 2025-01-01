from flask import Flask, render_template, request, jsonify
import re
from zxcvbn import zxcvbn

app = Flask(__name__)

# Load wordlist
def load_wordlist(filepath):
    with open(filepath, 'r') as file:
        return set(line.strip().lower() for line in file)

wordlist = load_wordlist("wordlist.txt")

# Password strength checker function
def password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short"
    if not re.search(r'[a-z]', password):
        return "Weak: Include at least one lowercase letter"
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter"
    if not re.search(r'[0-9]', password):
        return "Weak: Include at least one number"
    if not re.search(r'[@$!%*?&]', password):
        return "Weak: Include at least one special character"
    if password.lower() in wordlist:
        return "Weak: This password is in a common wordlist"

    zxcvbn_result = zxcvbn(password)
    if zxcvbn_result['score'] < 3:
        return "Weak: This is similar to commonly used patterns"

    return "Strong: Password meets the strength requirements"

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")
    result = password_strength(password)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
