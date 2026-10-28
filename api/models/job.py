from extensions import db
from datetime import datetime
import enum 

class JobStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED =  "failed"

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer , primary_key = True)
    type = db.Column(db.String(50), nullable = False)
    payload = db.Column(db.JSON,nullable = False)
    status = db.Column(db.Enum(JobStatus),default = JobStatus.PENDING, nullable = False)
    attempts = db.Column(db.Integer, default = 0, nullable = False )
    max_attempts = db.Column(db.Integer , default = 3 , nullable = False )
    run_at = db.Column(db.DateTime , nullable = False , default = datetime.utcnow,index = True)
    error = db.Column(db.Text , nullable = True)
    created_at = db.Column(db.DateTime , default = datetime.utcnow , nullable = False)
    updated_at = db.Column(db.DateTime ,  default = datetime.utcnow , nullable = False , onupdate = datetime.utcnow)
    