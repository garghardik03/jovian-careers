from sqlalchemy import create_engine,text
import os

db_connection_string="DB"
engine=create_engine(db_connection_string,connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})
with engine.connect() as conn:
  result=conn.execute(text("select * from jobs"))
  job=[]
  for row in result.all():
    job.append(dict(row))

print(job)