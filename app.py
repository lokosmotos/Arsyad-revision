from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/imlak")
def imlak():
    return render_template("imlak.html")

# Add routes for other topics similarly

if __name__ == "__main__":
    app.run(debug=True)
