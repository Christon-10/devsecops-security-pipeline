from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my DevSecOps Application!"


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/about")
def about():
    return {
        "project": "Automated DevSecOps Pipeline",
        "version": "1.0"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)