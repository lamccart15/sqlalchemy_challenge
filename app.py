# Import flask
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
import pandas as pd 
import datetime as dt
import numpy as np

# Create engine 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()` and reflect tables
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create and define routes
app = Flask (__name__)

# Define endpoint
@app.route("/")
def home():
    return (f"Surfs Up! A Look Into SQLAlchemy<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    last_year = dt.date(2017,8, 23) - dt.timedelta(days=365)
    sel = [Measurement.date, Measurement.prcp]
    precipitation_results = session.query(*sel).\
        filter(Measurement.date >= last_year).all()
    return jsonify (precipitation_results)
    session.close()

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_results = session.query(Station.station).all()
    return jsonify (stations_results)
    session.close()

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_year = dt.date(2017,8, 23) - dt.timedelta(days=365)
    sel = [Measurement.date, Measurement.tobs]
    tobs_results = session.query(*sel).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= last_year).all()
    return jsonify(tobs_results)
    session.close()

@app.route("/api/v1.0/<start>")
def start(start):
    session=Session(engine)
    temp_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    return jsonify(temp_results)
    session.close()

@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    session = Session(engine)
    temp_results_2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    return jsonify(temp_results_2)
    session.close()

if __name__ == '__main__':
    app.run(debug=True)