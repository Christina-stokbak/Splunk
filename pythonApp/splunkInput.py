import splunklib.client as client
import json

HOST = "localhost"
PORT = 8089  # Splunk management port
USERNAME = "admin"
PASSWORD = "AdminPass"

# Connect to Splunk service
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

event_data = {
    "event": "This is a sample event",
    "sourcetype": "custom_sourcetype",
    "index": "main",
    "host": "python_script_host",
    "_time": "2024-11-06T12:00:00"
}

# Get the target index
index = service.indexes["main"]

# Index the event
index.submit(event_data["event"], sourcetype=event_data["sourcetype"], host=event_data["host"])
print("Event successfully added to Splunk.")
