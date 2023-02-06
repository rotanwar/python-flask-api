from flask import Flask, Response, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return Response("Hello, world! (GAMMA)", status=200)


@app.route("/alpha")
def alpha():
    return Response("Hello, world! (ALPHA)", status=200)


@app.route("/beta/<key>")
def beta(key):
    if key == "fail":
        return Response("Failed! :_(", status=400)
    else:
        return Response("Hello, world! (BETA)", status=200)


@app.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("say_hello") is True:
        output = jsonify({"message": "Hello!"})
    else:
        output = jsonify({"message": "..."})

    return output


@app.route("/health")
def health():
    return Response("OK", status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)