# SQLAlchemy Project - Surfs Up!

![image](https://user-images.githubusercontent.com/69601778/118567612-f3b27380-b72a-11eb-9113-eb85d8d20363.png)

## Step 1 - Climate Analysis and Exploration

To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Used the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.

* Established a theoretical vacation range.

* Used SQLAlchemy `create_engine` to connect to a sqlite database.

* Used SQLAlchemy `automap_base()` to reflect tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

![image](https://user-images.githubusercontent.com/69601778/118567807-5277ed00-b72b-11eb-9687-172f3064091b.png)

* Used Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/69601778/118567788-49871b80-b72b-11eb-8478-3fcd37080e63.png)

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

  * Determined which station has the highest number of observations, using `func.min`, `func.max`, `func.avg`, and `func.count` in queries.

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Plotted the results as a histogram with `bins=12`.

![image](https://user-images.githubusercontent.com/69601778/118567941-9965e280-b72b-11eb-93db-3afd4044c0ed.png)


- - -

## Step 2 - Climate App

After completing the initial analysis, I designed a Flask API based on the queries that I developed.

### Routes

* `/`

  * Home page.

  * Lists all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.
  
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

![image](https://user-images.githubusercontent.com/69601778/118568039-cf0acb80-b72b-11eb-84a1-81759b6178ef.png)
