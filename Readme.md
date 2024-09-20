# Here I will list down all my learnings of Requests and BeautifulSoup library in Python

# How does Request Works?
## request only get the status code and not the data for data we have to inspect the beautiful soup

# Why do we use header in request.get?
## Header specifies the browser that request is coming from genuine user and tell the browser from which operating System the request is Coming.

# How to run Webscraper
## Start your pgadmin and create the database and perform the normal configuration in config.py

# Code Structure For This Project

# Scrape.py - To Scrape Data 
## return Properties [{},{}]

# Config.py - To connect Database
## Create a Connection with database and return conn

# store.py - It is used to store data
# here cursor is required to execute the query in pgadmin and %s are the parameterized queries where the dynamic value from the properties array get inserted

# export.py - It is used to generate the csv file
