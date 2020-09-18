from flask import Flask, request

app = Flask(__name__)

# get e' implicito, non serve specificarlo
@app.route("/", methods=["GET"])
def index():
    return 'Hello world'


@app.route("/post", methods=["POST"])
def post():
    print(request.form)
    return request.form


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
