from flask import Flask, request, jsonify

app = Flask(__name__)


data = [
    {"id": 0, "name": "test0"},
    {"id": 1, "name": "test1"},
    {"id": 2, "name": "test2"},
]


def searchById(id: int):
    for item in data:
        if item['id'] == id:
            return item
    return None

# get e' implicito, non serve specificarlo
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        'data': data
    })


@app.route("/<int:id>")
def get(id):
    return jsonify({
        'data': searchById(id)
    })


if __name__ == "__main__":
    app.run(debug=True)
