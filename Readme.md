Password Strength Checker
A web-based application to evaluate password strength using multiple checks, including custom criteria, a wordlist, zxcvbn analysis, and the "Have I Been Pwned" API.

Features
Basic Checks:
      Ensures the password contains:
      At least 8 characters.
      Uppercase and lowercase letters.
      Numbers and special characters.
Common Password Detection:
      Checks against a custom wordlist of commonly used passwords.
Advanced Analysis:
      Utilizes the zxcvbn library for robust password strength estimation.
Security Breach Check:
      Verifies if the password has been compromised using the "Have I Been Pwned" API.


Project Structure


password-checker/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── wordlist.txt               # File containing common passwords
│
├── templates/
│   └── index.html             # HTML file for the frontend
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS for styling
│   ├── js/
│   │   └── script.js          # JavaScript for client-side logic
│   └── img/                   # (Optional) Images folder if needed
│
└── README.md                  # Project description



Getting Started
1. Clone the Repository

git clone <repository_url>
cd password-checker

2. Install Dependencies
Make sure you have Python 3.7+ installed. Then run:

pip install -r requirements.txt

3. Run the Application
python app.py


4. Open in Browser
Navigate to: http://127.0.0.1:5000

How It Works

Enter a password into the input field.
The system performs:
     Length and character-type checks.
     Comparison against a list of common passwords.
     Strength analysis via zxcvbn.
     Data breach check using "Have I Been Pwned" API.
     Displays a result indicating the password's strength and improvement suggestions.
Dependencies
     Flask: Backend web framework.
     zxcvbn: Advanced password strength checker.
     requests: For interacting with the "Have I Been Pwned" API.


 Install them using:

  pip install Flask zxcvbn requests


Future Enhancements
    Add support for additional languages.
    Extend password breach checks for offline usage.
    Include user feedback for real-time password improvements.
License
This project is licensed under the MIT License. See the LICENSE file for details.
