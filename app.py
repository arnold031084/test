from flask import Flask, request, jsonify
from prime import is_prime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Prime Number Checker</h2>
    <form action="/check" method="get">
        <input type="number" name="number" required>
        <button type="submit">Check</button>
    </form>
    """

@app.route("/check")
def check_prime():
    try:
        number = int(request.args.get("number"))
        result = is_prime(number)

        return jsonify({
            "number": number,
            "is_prime": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
