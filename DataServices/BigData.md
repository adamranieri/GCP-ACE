# Big Data Lifecycle
1. Ingest
    -  Get the data from somewhere
2. Store
    - House the data somewhere
3. Process/Analyze
    - Filter and refine the data
4. Explore and Visualize
    - Make the data Human Friendly to make decisions  

# Cloud IoT
- Googles Internet of Things service

# Cloud Pub/Sub
- Infinitely scalable messaging system for ingestion
- Global service
- A **Topic**  is essentially a queue for messages
- A **Publisher** creates messages to be put in a topic
- A **Subsciber** conssumes messages from a topic
- Great for asynchronus workloads and as shock absorber
- Decouples applications and is a great "glue" service
- 10MB max per message
- Messages are stored for 7 days but no Dead Letter Queue
    - DLQ is a topic that is for unprocessable messages
- Push Mode
    - Topic recieves a message and sends it to subscribers 
    - Done over HTPPS
    - Slow Start means pus/sub will slowly ramp up deliveries as it gets back successes
- Pull Mode
    - Subscribers while poll the topic ever x seconds to get pending messages
    - Subscribers must acknowledge that a message has been handled before it disappears from the topic.
    - Can get messages in batches or long polling
- Pay for data volume

# Cloud Data Prep
- ETL system
- Data wrangling tools for business analyts
- More like matlab or excel in use case

# Dataproc
- MapReduce processing
    - MapReduce is a data processing programming paradigm
    - Primarily used for process massive data loads in parallel
- Used to set up Apache Spark or Hadoop clusters that *already exist*
- Use Dataflow if starting brand new

# Cloud Datalab
- Smartly autoscaled stream and MapReduce processing

# Datalab
- Data exploration and visualization tool
- Uses Jupyter notebook

# Cloud Datastudio
- Creates dashboards for data reporting

# Cloud Genomics
- Specifically for genetics and life science experiments
- Requestor pays price model
    - You pay for storing the data but people who use it pay for data transfer costs