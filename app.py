import os
from flask import (
    Flask, flash, request, render_template,
    redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    breads = list(mongo.db.breads.find())
    return render_template("home.html", breads=breads)


@app.route("/display_breads")
def display_breads():
    breads = list(mongo.db.breads.find())
    flash("All Breads")
    return render_template("display_breads.html", breads=breads)


@app.route("/display_recipe")
def display_recipe():
    return render_template("display_recipe.html")


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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
