from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    specialty = db.Column(db.String(100))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(db.Integer)
    patient_id = db.Column(db.Integer)

    date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

def create_appointment(doctor_id, patient_id):
    appo = Appointment(
        doctor_id=doctor_id,
        patient_id=patient_id
    )

    db.session.add(appo)
    db.session.commit()

with app.app_context():
    db.create_all()

    d1 = Doctor(name="Ali", specialty="Cardiology")
    p1 = Patient(name="Vali")

    db.session.add_all([d1, p1])
    db.session.commit()

    create_appointment(1, 1)
