from flask_pymongo import PyMongo
from flask import Flask
app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/Jovian"
#how to check if the database is connected
mongo=PyMongo(app)
print(mongo.db)
JOBS=mongo.db.Jobs.find() # JOBS is a cursor
jobs=[job for job in JOBS] # jobs is a list
print(jobs)