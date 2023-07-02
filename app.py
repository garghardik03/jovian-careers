from flask import Flask,render_template, jsonify
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/Jovian"
mongo=PyMongo(app)
# JOBS=[
#   {
#     "id":1,
#     "title":"Data Analyst",
#     "Location":"Bengaluru, India",
#     "Salary":"1000000"
#   },
#   {
#     "id":2,
#     "title":"Data Scientist",
#     "Location":"Delhi, India",
#     "Salary":"1500000"
#   },
#   {
#     "id":3,
#     "title":"Frontend Engineer",
#     "Location":"Remote",
#     "Salary":"1200000"
#   }
# ]



@app.route("/")
def hello_world():
  jobs=mongo.db.Jobs.find()
  JOBS=[job for job in jobs]
  return render_template("home.html",jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    jobs=mongo.db.Jobs.find()
    JOBS=[job for job in jobs]
    return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  jobs=mongo.db.Jobs.find()
  JOBS=[job for job in jobs]
  job=JOBS[id]
  return jsonify(job)
  
  
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True,port=5001)