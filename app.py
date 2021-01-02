import os
from flask import (
    Flask, flash, request, render_template,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    breads = list(mongo.db.breads.find().sort("name", 1))
    return render_template("home.html", breads=breads)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
    return render_template("register.html")


@app.route("/display_breads")
def display_breads():
    breads = list(mongo.db.breads.find().sort("name", 1))
    flash("All Breads")
    return render_template("display_breads.html", breads=breads)


@app.route("/display_recipe/<bread_id>")
def display_recipe(bread_id):
    bread = mongo.db.breads.find_one({"_id": ObjectId(bread_id)})
    return render_template("display_recipe.html", bread=bread)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        bread = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "country": request.form.get("country"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "cooking_temp": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "image_url": request.form.get("url")
        }
        mongo.db.breads.insert_one(bread)
        flash("New Bread Recipe Received - Thankyou!")
        return redirect(url_for('display_breads'))
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<bread_id>", methods=["GET", "POST"])
def edit_recipe(bread_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "country": request.form.get("country"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "cooking_temp": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "image_url": request.form.get("url")
        }
        mongo.db.breads.update({"_id": ObjectId(bread_id)}, submit)
        flash("Recipe Updated - Thankyou!")
        # return redirect(url_for('display_breads'))

    bread = mongo.db.breads.find_one({"_id": ObjectId(bread_id)})
    return render_template("edit_recipe.html", bread=bread)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
