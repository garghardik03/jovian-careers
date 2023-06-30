from flask import Flask,render_template, jsonify
app=Flask(__name__)

JOBS=[
  {
    "id":1,
    "title":"Data Analyst",
    "Location":"Bengaluru, India",
    "Salary":"1000000"
  },
  {
    "id":2,
    "title":"Data Scientist",
    "Location":"Delhi, India",
    "Salary":"1500000"
  },
  {
    "id":3,
    "title":"Frontend Engineer",
    "Location":"Remote",
    "Salary":"1200000"
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)
  
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)