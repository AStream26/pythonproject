# pythonproject
project on python 
 project uses google geocoding API to know the latitude and longitude of different address that is provided in 
 where.data and the geodata is then dumped into the a sqlite file
 
once the data is dumped in sql. The data from sqlite file is once again read by another python file and the latitude and longitude 
of different location is written in a js file.

IN html file,  a Gmap is created and the location stored in js file is looped and pointer mark the
exact position in Gmap.
