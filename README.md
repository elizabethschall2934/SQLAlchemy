# SQLAlchemy
Climate Analysis and Exploration

The purpose of this activity was to use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. 

Technologies: SQLAlchemy ORM queries, Pandas, Jupyter Notebook, and Matplotlib.

The provided sqlite files were used to choose a start date and end date for the trip, and ultimately complete the climate analysis and data exploration.

Requirements:
Vacation range approximately 3-15 days total.

Tasks performed:

Use SQLAlchemy create_engine to connect to the sqlite database.
Use SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.

Precipitation Analysis

Design a query to retrieve the last 12 months of precipitation data.
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.
Use Pandas to print the summary statistics for the precipitation data.

Station Analysis

Design a query to calculate the total number of stations.
Design a query to find the most active stations.
List the stations and observation counts in descending order.
Which station has the highest number of observations?
Design a query to retrieve the last 12 months of temperature observation data (TOBS).
Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12.

Climate App

Design a Flask API based on the queries that were developed.

Use Flask to create the routes.
List all routes that are available.
Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of the dictionary.
Return a JSON list of stations from the dataset.
Query the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
