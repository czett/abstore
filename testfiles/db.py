from pymongo import MongoClient
import pymongo

cluster = MongoClient("mongodb+srv://bepisdev:vM7PmGUCkvgW5MwL@cluster0.nu6exm4.mongodb.net/?retryWrites=true&w=majority")

db = cluster["abstore"]
login = db["login"]
userdata = db["userdata"]

login.insert_one({"_id":23845,"name":"amogus"})