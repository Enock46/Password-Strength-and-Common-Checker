from flask import Flask, render_template, request, jsonify
import re
import hashlib
from zxcvbn import zxcvbn
import requests

app = Flask(__name__)

# Load wordlist (common passwords)
def load_wordlist(filepath):
    with open(filepath, 'r') as file:
        return set(line.strip().lower() for line in file)

wordlist = load_wordlist("wordlist.txt")

# Password strength checker function
def password_strength(password):
    # Check for length of password
    if len(password) < 8:
        return "Weak: Password is too short"

    # Check for lowercase character
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase"

    # Check for uppercase character
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase"

    # Check for special character
    if not re.search(r'[@$!%*?&]', password):
        return "Weak: Password should contain at least one special character"

    # Check for number
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one number"

    # Check if password is too common
    if password.lower() in wordlist:
        return "Weak: Password is too common"

    # Check using zxcvbn
    zxcvbn_result = zxcvbn(password)
    if zxcvbn_result['score'] < 3:
        return "Weak: This password is too simple or contains common patterns"

    # Check if password is breached
    pwned_result = pwned_check(password)
    if pwned_result != "Pass":
        return pwned_result

    return "Strong: Password is secure!"


# Function to check if password is in the "Pwned Passwords" database
def pwned_check(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(':')
            if suffix == hash_suffix:
                return f"Weak: Password has been breached {count} times"
    return "Pass"  # Password not found in breached list


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
