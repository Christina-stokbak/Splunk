import splunklib.client as client
import splunklib.results as results

HOST = "localhost" 
PORT = 8089 # Default management port for Splunk
USERNAME = "admin" 
PASSWORD = "AdminPass" 

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    scheme="https"
)

print("Connected to Splunk:", service.apps)

# Define your search query (e.g., to get last 24 hours of logs)
search_query = "search sourcetype=\"custom_sourcetype\" | head 1"

# Run the search job
job = service.jobs.create(search_query, output_mode="json")

# Wait for the job to complete
while not job.is_done():
    job.refresh()

# Retrieve results
for result in results.JSONResultsReader(job.results(output_mode="json")):
    print("time: ", result.get("_time"))
    print("source: ", result.get("source"))
    print(result.get("index"))
