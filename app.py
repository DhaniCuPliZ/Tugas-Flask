from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_text = request.form.get("textfield")
    return f"Anda mengirimkan: {input_text}"

if __name__ == "__main__":
    app.run(debug=True)