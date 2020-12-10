# PythonWebScraper
- Takes in a file name as `keywords` that reads and stores the search words that will be searched on the Unpaywall database.
- Requestor class handles methods such as `request_url, get_method_query_request_url` and `get_up_to_x_pages_of_query`.
- The scraper accesses the database and filters the data received. The data will be removed of properties that currently appear to be unusable.
- Once each scraper filters and checks for duplicate articles, it connects to Elasticsearch and appends the filtered data to the AMR index.
