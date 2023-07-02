from flask import Flask,render_template, jsonify,request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/Jovian"
mongo=PyMongo(app)

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

@app.route("/jobs/<title>")
def get_job(title):
    job = mongo.db.Jobs.find_one({"title": title})
    if job:
        return render_template("job_page.html", job=job)
    else:
        return jsonify({"error": "Job not found"})


@app.route("/job/<title>/apply",methods=["POST"])
def apply(title):
  data=request.form
  job=mongo.db.Jobs.find_one({"title":title})
  if job:
    #convert data to list of dictionaries
    answer=[{"name":data["First Name"],"email":data["Email"],"resume":data["Resume Url"]}]
    #insert to db
    mongo.db.Applications.insert_one({"job":job["title"],"applications":answer})
    print("Application received")
    return render_template("apply.html",job=job,application=data)
    #convert data to json and save to database
  else:
    return jsonify({"error":"Job not found"})


if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True,port=5001)