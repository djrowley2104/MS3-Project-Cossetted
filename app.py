import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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

@app.route("/get_tasks")
def get_tasks():
    sale_items = list(mongo.db.Sale_Item.find())
    return render_template("tasks.html", Sale_Item=sale_items)

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for('profile', username=session['user']))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("classics.html", username=username)


@app.route("/sellclassic", methods=["GET", "POST"])
def sellclassic():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"] })
        approved = "approved" if request.form.get("approved") else "off"
        task = {
            "Sellers_Class": request.form.get("Sellers_Class"),
            "Sellers_Name": request.form.get("Sellers_Name"),
            "Sellers_Phone_Number": request.form.get("Sellers_Phone_Number"),
            "Email_Address": request.form.get("Email_Address"),
            "Item_For_Sale": request.form.get("Item_For_Sale"),
            "Manufacturer": request.form.get("Manufacturer"),
            "Model": request.form.get("Model"),
            "Engine_Size": request.form.get("Engine_Size"),
            "Description_Of_Item": request.form.get("Description_Of_Item"),
            "Photo": request.form.get("Photo"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.Sale_Item.insert_one(task)
        flash("Classic Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.saletype.find()
    return render_template("sellclassic.html", saletype=categories)

# add new sales task for item
@app.route("/sellitem", methods=["GET", "POST"])
def sellitem():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"] })
        task = {
            "Sellers_Class": request.form.get("Sellers_Class"),
            "Sellers_Name": request.form.get("Sellers_Name"),
            "Sellers_Phone_Number": request.form.get("Sellers_Phone_Number"),
            "Email_Address": request.form.get("Email_Address"),
            "Item_For_Sale": request.form.get("Item_For_Sale"),
            "Manufacturer": request.form.get("Manufacturer"),
            "Model": request.form.get("Model"),
            "Engine_Size": request.form.get("Engine_Size"),
            "Description_Of_Item": request.form.get("Description_Of_Item"),
            "Photo": request.form.get("Photo"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.Sale_Item.insert_one(task)
        flash("Spares Successfully Added")
        return redirect(url_for("get_tasks"))

    categories = mongo.db.saletype.find()
    return render_template("sellitem.html", saletype=categories)    

@app.route("/edit_classic/<task_id>", methods=["GET", "POST"])
def edit_classic(task_id):
    categories = mongo.db.saletype.find()
    task = mongo.db.Sale_Item.find_one({"_id": ObjectId(task_id)})
    return render_template("sellitem_edit.html", task=task, saletype=categories)

@app.route("/edititem/<task_id>", methods=["GET", "POST"])
def edititem(task_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"] })
        update = {
            "Sellers_Class": ObjectId(request.form.get("saletype")),
            "Sellers_Name": request.form.get("Sellers_Name"),
            "Sellers_Phone_Number": request.form.get("Sellers_Phone_Number"),
            "Email_Address": request.form.get("Email_Address"),
            "Item_For_Sale": request.form.get("Item_For_Sale"),
            "Manufacturer": request.form.get("Manufacturer"),
            "Model": request.form.get("Model"),
            "Engine_Size": request.form.get("Engine_Size"),
            "Description_Of_Item": request.form.get("Description_Of_Item"),
            "Photo": request.form.get("Photo"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.Sale_Item.update({"_id": ObjectId(task_id)}, update)
        flash("Spares Successfully Updated")
        return redirect(url_for("get_tasks"))
        
    categories = mongo.db.saletype.find()
    task = mongo.db.Sale_Item.find_one({"_id": ObjectId(task_id)})
    return render_template("sellitem_edit.html", task=task, saletype=categories)

@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.Sale_Item.remove({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)