from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import backend
from backend import send_email

def email_exists(email):
    for i in backend.email():
        for emails in i:
            if emails == email:
                return "True"

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ["POST"])
def success():
    if request.method == 'POST':
        email = request.form["email_address"]
        height = request.form["height"]
        if(email_exists(email) == 'True'):
            return render_template("index.html", text1 = "This email address is already used !")
        else:
            backend.insert(email, height)
            send_email(email, backend.height_average())
            return render_template("success.html")





if __name__ == '__main__':
    app.debug = True
    app.run()


