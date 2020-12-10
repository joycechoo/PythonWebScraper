# PythonWebScraper
Takes in a file name as keywords that reads and stores the search words that will be searched on the CORE database.
Requestor class handles methods such as request_url, get_method_query_request_url, and get_up_to_x_pages_of_query.
The scraper accesses the database and filters the data received. The data will be removed of properties that currently appear to be unusable.
Once the data is cleaned, the scraper will connect to Elasticsearch and add each of the filtered data into the AMR index.
