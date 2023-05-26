# REST API Challenge

This API have a few endpoints:
- ``/`` (GET): The index page with a form to insert table name and a csv file;
- ``/data`` (GET, POST): The endpoint which calls the methods that insert the csv in the table given at the aforementioned endpoint;
- ``/hired_above_average1`` (GET): This endpoint cointain a table with all the ids and names of the departments that hired more employees than the 2021's average.

This API is hosted on AWS on this address (3.91.238.76:5000). I didn't have the time to set up a DNS.
This app is also dockerized with the app in python, using flask to set up the api and the basic web pages and with a postgresql database.

Docker compose was used to create a stack and the connections between the containers and to make the process of setting up the database container easier.