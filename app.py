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
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # check hashed password against users' input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(
                    url_for('profile', username=session["user"]))
            else:
                # passwords dont match
                flash("Username and/or Password don't match")
                return redirect(url_for('login'))
        else:
            # username not found!
            flash("Username and/or Password don't match")
            return redirect(url_for('register'))

    return render_template("login.html")


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
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("register.html")


@app.route("/home")
def home():
    breads = list(mongo.db.breads.find().sort("name", 1))
    return render_template("home.html", breads=breads)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session users' username from database for their profile page
    # username = mongo.db.users.find_one(
    #     {"username": session["user"]})["username"]
    # match bread recipe in db with currently logged user and display results
    current_user = session["user"]
    user_recipe = list(mongo.db.breads.find(
        {"author": current_user.lower()}))
    if user_recipe:
        # if user is logged in, display profile page with users' recipes
        return render_template(
            "profile.html", breads=user_recipe,
            username=username.capitalize())
    else:
        flash("No Bread Recipes Listed Yet!")
        return render_template(
            "profile.html", username=username.capitalize())


@app.route("/display_breads")
def display_breads():
    # sort the names of the breads list #
    breads = list(mongo.db.breads.find().sort("name", 1))
    flash("All Breads")
    return render_template("display_breads.html", breads=breads)


@app.route("/display_recipe/<recipe_id>")
def display_recipe(recipe_id):
    bread = mongo.db.breads.find_one({"_id": ObjectId(recipe_id)})
    return render_template("display_recipe.html", bread=bread)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        author = mongo.db.users.find_one({"username".lower()})

        bread = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "country": request.form.get("country"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "cooking_temp": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "image_url": request.form.get("url"),
            "author": author,
            "is_featured": request.form.get("is_featured")
        }
        mongo.db.breads.insert_one(bread)
        flash("New Bread Recipe Received - Thankyou!")
        return redirect(url_for('display_breads'))
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "country": request.form.get("country"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "cooking_temp": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "image_url": request.form.get("url"),
            "is_featured": request.form.get("is_featured")
        }
        mongo.db.breads.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated - Thankyou!")
        # return redirect(url_for('display_breads'))

    bread = mongo.db.breads.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", bread=bread)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.breads.remove({"_id": ObjectId(recipe_id)})
    flash("Bread Recipe Successfully Deleted")
    return redirect(url_for('home'))


@app.route("/logout")
def logout():
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
