from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", name="boss")

@app.route('/about')
def about():
    return render_template("about.html", name="boss")

@app.route('/contact')
def contact():
    return render_template("contact.html", name="boss")

if __name__ == "__main__":
    app.run(debug=True)