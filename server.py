from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def show_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("read_all.html", users = users)

@app.route("/user/new")
def display_create_user():
    return render_template("create.html")

@app.route("/user/new", methods = ['POST'])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }

    User.create(data)

    return redirect("/user/new")

if __name__ == "__main__":
    app.run(debug=True)