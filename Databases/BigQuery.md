# BigQuery
- Serverless data warehouse for analytics via SQl
- BigQuery is not for transactions or web applications
    - You should only be doing reads essentially
    - Along with data streams/dumps into BigQuery
- Pay for   
    - Gigabytes stored
    - Gigabytes scanned
    - Streaming inserts

```bash
    bq extract --destination_foramt json --compression GZIP 'mydata.sometable' gs://mybucket/data.zip
    # --dry_run will NOT execute the query but will tell you how much data will be processed
    bq query --dry_run --nouse_legacy_sql "SELECT * FROM `bigquery-public-data`.samples.shakespeare"

    bq load --autodetect --source_format=CSV mydata.sometable gs://mybucket/mydata.csv

    
```