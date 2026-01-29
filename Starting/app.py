from flask import Flask

'''
Create a flask app
'''
### WSGI
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to the Flask App! , i am here to learn Flask."

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ == "__main__":
    app.run(debug=True)
