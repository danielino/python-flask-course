from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    data = json.loads(request.data)
    print(data)
    return "Hello World"

app.run(debug=True)
