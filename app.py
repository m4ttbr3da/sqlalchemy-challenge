import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all dates and prcp values."""
    
    # Perform a query to retrieve the precipitation data in the last one year
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date>='2016-08-23').\
    order_by(Measurement.date.desc()).all()

    session.close()
    
    # Create a dictionary from the row data and append to list of prcp_one_year
    prcp_one_year = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['precipitation'] = prcp
        prcp_one_year.append(prcp_dict)


    return jsonify(prcp_one_year)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all stations."""
    
    # Perform a query to retrieve all of the stations in the data set
    results = session.query(Measurement.station.distinct().label("station"))
    stations = [row.station for row in results.all()]

    session.close()
    
    # Return list as JSON
    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def most_active_temps():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    """Return a list of all stations."""
    
    # Perform a query to retrieve the temperature data in the last one year as recorded by the msot active station
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
    filter(Measurement.date >= '2016-08-23').filter(Measurement.station == "USC00519281").\
    order_by(Measurement.date.desc()).all()

    session.close()
   
    
    # Create dictionary from the row data and append to list of most_active_temps
    
    most_active_temps = []
    for date, tobs, station in results:
        temps_dict = {}
        temps_dict['date'] = date
        temps_dict['temperature'] = tobs
        temps_dict['station'] = station
        most_active_temps.append(temps_dict)
    
    return jsonify(most_active_temps)

@app.route("/api/v1.0/<start>")
def timestart(start):
    start_time = start
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Returns min, max, and averages from the specified start date to the latest date in the data set

    results = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_time).\
        group_by(Measurement.date).all()
 
    session.close()
    
    timerange_list = list(np.ravel(results))
    return jsonify(timerange_list)

@app.route("/api/v1.0/<start>/<end>/")
def timerange(start, end):
    start_time = start
    end_time = end
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Returns min, max, and averages for the range specified by start and end dates

    results = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_time).filter(Measurement.date <= end_time).\
        group_by(Measurement.date).all()
   
    session.close()
    
    timerange_list = list(np.ravel(results))
    return jsonify(timerange_list)

if __name__ == '__main__':
    app.run(debug=True)