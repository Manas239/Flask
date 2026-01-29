#Building URl Dyanamically
#variable rules
#jinja 2 template engin

###Jinja 2 template engine there is multiple ways to read data source from backend
'''
Docstring for Starting.jinja
.
{{ }} expression in print output in html
{%...%} condition , for loop
{#...#} comment
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask App!</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("form.html")

# Variable rule + dynamic URL
#if condition
@app.route("/success/<int:score>")
def success(score):
    return render_template("result.html", score=score)





if __name__ == "__main__":
    app.run(debug=True)
