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



# Cloud Data Prep
- ETL system
- Data wrangling tools for business analyts
- More like matlab or excel in use case

# Dataproc
- Not a database
- It processes data, it doesn't keep it
- MapReduce processing
    - MapReduce is a data processing programming paradigm
    - Primarily used for process massive data loads in parallel
- Used to set up Apache Spark or Hadoop clusters that *already exist*
- Use Dataflow if starting brand new


```bash
    gcloud dataproc clusters create my-cluster
    gcloud dataproc jobs submit spark my-job
```

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