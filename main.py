import pymongo, datetime, string, random
from pymongo import MongoClient
from flask import Flask, render_template, redirect, request, url_for, session
import abtools as at

app = Flask(__name__)
app.secret_key = "ligrhued"
cluster = MongoClient("mongodb+srv://bepisdev:vM7PmGUCkvgW5MwL@cluster0.nu6exm4.mongodb.net/?retryWrites=true&w=majority")

db = cluster["abstore"]
login = db["login"]
userdata = db["userdata"]

def update(collection, query, newvals):
	collection.update_one(query, {"$set": newvals})

def create_uuid(length):
	letters = string.ascii_lowercase
	uuid = ''.join(random.choice(letters) for i in range(length))

	uen = login.find_one({"_id":uuid})

	while True:
		if uen == None:
			break
		else:
			length = 8
			letters = string.ascii_lowercase
			uuid = ''.join(random.choice(letters) for i in range(length))
			uen = login.find_one({"_id":uuid})

	return uuid

def uuid_to_name(uuid):
	name = userdata.find_one({"_id":uuid})["name"]

	return name

@app.route("/")
def home():
	try:
		return render_template("index.html", logged_in=session["logged_in"], un=session["uname"])
	except:
		session["logged_in"] = False
		return render_template("index.html", logged_in=session["logged_in"])

@app.route("/register")
def render_register():
	return render_template("logreg.html", action="r")

@app.route("/login")
def render_login():
	return render_template("logreg.html", action="l")

@app.route("/login/process", methods=["POST"])
def processlogin():
	un = request.form["lname"]
	up = request.form["lpass"]


	uen = login.find_one({"name":un}) # uen for userentry

	if uen == None:
		return render_template("logreg.html", action="l", message="This account doesn't exist. Check your spelling or quickly create an account.")
	else:
		if uen["pw"] == up:
			session["uuid"] = uen["_id"]
			session["uname"] = un
			session["logged_in"] = True
			return redirect("/")
		else:
			return render_template("logreg.html", action="l", message="Wrong password.")

@app.route("/register/process", methods=["POST"])
def processregister():
	un = request.form["rname"]
	up = request.form["rpass"]

	uen = login.find_one({"name":un}) # uen for userentry

	if uen == None:
		uuid = create_uuid(12)
		rdata = {"_id":uuid,"name":un,"pw":up}
		login.insert_one(rdata) # rdata for register data

		userdata.insert_one({"_id":uuid,"name":un})

		session["uuid"] = uuid
		session["uname"] = un
		session["logged_in"] = True
		return redirect("/")
	else:
		return render_template("logreg.html", action="r", message="This account already exists. Log in or enter a different username to register your own account.")

@app.route("/logout")
def logout():
	session["loggedin"] = False
	session.clear()
	return redirect("/")

# Specific part begins here

@app.route("/plan/create/overview")
def plan_overview():
	try:
		if session["logged_in"] == False:
			return redirect("/")
	except:
		return redirect("/")

	return render_template("plan_create_overview.html", name=session["uname"])

@app.route("/plan/create/form")
def create_plan_form():
	try:
		if session["logged_in"] == False:
			return redirect("/")
	except:
		return redirect("/")

	return render_template("plan_create_form.html", name=session["uname"])

@app.route("/plan/process-form", methods=["POST"])
def process_form():
	try:
		if session["logged_in"] == False:
			return redirect("/")
	except:
		return redirect("/")


	unit = request.form["which-unit"]

	if unit == "imperial":
		lbs = request.form["weight"]
		oz = request.form["ounces"]
		weight = round(at.lbs_to_kg(float(lbs), float(oz)))

		ft = request.form["height"]
		inc = request.form["inches"]
		height = round(at.ft_to_cm(float(ft), float(inc)))
	else:
		weight = round(float(request.form["weight"]))
		height = round(float(request.form["height"]))
	
	gender = request.form["gender"]

	flvl = request.form["lvl"]
	goal = request.form["goals"] # eg losing/gaining weight
	tgoal = request.form["typegoal"] # eg muscular endurance, power/strength

	if flvl == 1:
		wlvl = "Beginner"
	elif flvl == 2:
		wlvl = "Intermediate"
	else:
		wlvl = "Advanced" # wlvl for word level since some methods use "beginner" instead of 1

	return "yes"

if __name__ == "__main__":
	app.run(debug=True)