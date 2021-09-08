# Monitoring and Logging

- Flow Logs
    - track http requests and data
    - Timestamp, bytes, IP address
- Audit Logs (Previously known as activity logs)
    - Record GCP activities
    - Who did what when
    - creating a firewall, creating an instance, adding a user
    - Types of logs
        - Configuration (commissing resources, editing permissions)
        - Billing
        - Data Access
        - Development (application logs)
        - Monitoring
- Cloud Logs (Previously stackdriver logs)
    - Application logs
    - Logs written by an application stored in the cloud
    - Only lasts 30 days
- Cloud Monitoring (Previously stackdriver monitoring)
    - Health checks and metrics of your GCP infrastructure
    - What is currently up and running, what is healthy, cpu usage, disk usage etc....
- Cloud Trace (Previously stackdriver trace)
    - Tracks and collects latency data
    - How long an endpoint takes to respond 
- Error Reporting
    - For logging stack traces in an application

### Other Types
- SQL binary logging
    - keeps a record of all transactions

# Log Sinks
- Logs can be sent to 3 locations
    - Big Query
    - Pub/Sub
    - Cloud Storage

# Cloud Billing API
- Programmtically mangage billing