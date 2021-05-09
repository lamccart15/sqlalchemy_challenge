# SQLAlchemy_Challenge


Climate analysis and data exploration was completed using Python and SQLAlchemy ORM queries.

The following is demonstrated in the files contained within this repository: 

## Climate Analysis and Exploration 

- SQLAlchemy was used to connect to the sqlite database and reflect tables into classes. 

- Python was linked to the database via a SQLAlchemy session.

- Precipitation Analysis:
- Most recent date in the data set was identified
- Last 12 months of precipitation data was compiled (including the date and precipitation values)
- The query results were loaded into a Pandas DataFrame and sorted by date
- A line plot was created to visualize the data
- Summary statistics were revealed 

- Station Analysis:
- Total number of stations in the dataset was identified
	- Stations and their observation counts were displayed in descending order
	- The most active station was identified
	- Lowest, highest, and average temperatures were calculated for the most active station
	- The last 12 months of temperature observation data (tobs) was revealed for the most active station
	- A histogram was created to visualize the data


## Climate App

A Flask API was designed based on the queries above. Within this API – the results were returned in JSON format. Routes include both static results (precipitation, stations, and tobs) as well as dynamic results (start and start/end dates). 






