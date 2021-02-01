from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"List all available api routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>")

# Precipitation API
@app.route("/api/v1.0/precipitation")
def precipitation():
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    year_rain = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_year).all()

    rain = {date: prcp for date, prcp in year_rain}

    return jsonify(rain)

# Stations API
@app.route("/api/v1.0/stations")
def stations():
    available = session.query(Station.station, Station.name).all()

    station = list(np.ravel(available))

    return jsonify(station)

# Temperature Observations API
@app.route("/api/v1.0/tobs")
def temp_obs():
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_query = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= year_ago).all()

    tobs = list(np.ravel(tobs_query))

    return jsonify(tobs)

# Start date API
@app.route("/api/v1.0/<start>")
def start_date(start):
    find_temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).all()


    temp = list(np.ravel(find_temps))

    return jsonify(temp)

# Start/End date API
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    range_temp =list(np.ravel(temps))

    return jsonify(range_temp)

if __name__ == "__main__":
    app.run(debug=True)