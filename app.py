from flask import Flask, request
from prime import is_prime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Prime Number Checker</title>
    </head>
    <body>
        <h2>Prime Number Checker</h2>
        <form action="/check" method="post">
            <input type="number" name="number" placeholder="Enter a number" required>
            <button type="submit">Check</button>
        </form>
    </body>
    </html>
    """

@app.route("/check", methods=["POST"])
def check_prime():
    try:
        number = int(request.form["number"])

        if is_prime(number):
            result = f"{number} is a Prime Number"
        else:
            result = f"{number} is Not a Prime Number"

        return f"""
        <html>
        <head>
            <title>Result</title>
        </head>
        <body>
            <h2>{result}</h2>
            <a href="/">Check Another Number</a>
        </body>
        </html>
        """

    except ValueError:
        return """
        <h2>Invalid Input</h2>
        <a href="/">Try Again</a>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
