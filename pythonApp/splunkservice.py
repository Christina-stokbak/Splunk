import splunklib.client as client
import splunklib.results as results

# Replace these with your actual Splunk server details
HOST = "localhost"       # e.g., "localhost" or "splunk.yourdomain.com"
PORT = 8000                   # Default management port for Splunk
USERNAME = "admin"      # Your Splunk username
PASSWORD = "AdminPass"      # Your Splunk password

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

print("Connected to Splunk:", service.apps)  # This will print installed apps

# Define your search query (e.g., to get last 24 hours of logs)
search_query = "search index=_internal | head 10"

# Run the search job
job = service().jobs.create(search_query)

# Wait for the job to complete
while not job.is_done():
    print("Waiting for search to complete...")
    job.refresh()

# Retrieve results
for result in results.ResultsReader(job.results()):
    print(result)
