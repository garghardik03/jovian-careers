from flask_pymongo import PyMongo
from flask import Flask
app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/Jovian"
mongo=PyMongo(app)
JOBS=mongo.db.Jobs.find()
jobs=[job for job in JOBS]
print(jobs)