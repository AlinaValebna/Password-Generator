from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def password_generator():
    password = ""
    if request.method == "POST":
        # Get user inputs
        length = int(request.form.get("length", 8))
        include_uppercase = "uppercase" in request.form
        include_lowercase = "lowercase" in request.form
        include_numbers = "numbers" in request.form
        include_symbols = "symbols" in request.form
        
        # Character pools
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
        
        # Combine selected pools
        character_pool = ""
        if include_uppercase:
            character_pool += uppercase_letters
        if include_lowercase:
            character_pool += lowercase_letters
        if include_numbers:
            character_pool += numbers
        if include_symbols:
            character_pool += symbols
        
        # Generate password
        if character_pool:
            password = "".join(random.choice(character_pool) for i in range(length))
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)