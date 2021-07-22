# GCS Google Cloud Storage
- Primary service for storing files/**objects**
    - Analogous to S3 for AWS
    - Objects are atomic units. It does cannot edit or read just part of an object
    - objects can be versioned
        - Lastest version is called the live version
- **Buckets** are a collection of objects
- Bucket names must be gloablly unique
- Files are private by default 
- To make files public you have to edit persmissions
    - add entity Group
    - name allUsers
- Many other services like AppEngine use GCS
- Buckets must be made for a geographic location
    - Multi-region
        - example United States
    - Dual-region
        - example Iowa and South Carolin
    - Region
        - Europe-north1
- Pick a location geographically near the resources that will be using itW
- Buckets locations cannot be edited once created.
    - To "edit" you should make a new bucket in the correct location
    
- Storage Classes
    - Buckets can be created for different storage accessiblity
    - Done to save money for less accessed files
    - All classes have a minium storage duration which is how long it must be in the bucket before being accessed *without* a cost penalty
    - All objects in storage are accessible in milleseconds *for a price*
    - In general you pay more for data transfer and less for data storage
    - Standard
        - For frequently updated/used
    - Nearline
        - Minimum duration 30 days
    - Coldline
        - Minimum duration  90 days
    - Archive
        - Minimum duration 365 days


## CLI Command
- **gsutil** is the tool for GCS commands

### Create a Bucket
```bash
    gsutil mb gs://bucketname
```

### List all buckets in project
```bash
    gsutil list
```

### List objects in bucket 
```bash
    gsutil list gs://bucketname
```
### Upload
```bash
    gsutil cp localfile gs://bucketname
```

### Download
```bash
    gsutil cp gs://bucketname/something.txt .
```

### Permissions (Access Control list )
```bash
    gsutil acl set 
    gsutil acl ch 
    gsutil acl get
    gsutil acl ch -u AllUsers:r gs://wassup/cheatsheet.png
    
```

#### Get metadata
```bash
    gsutil stat gs://bucketname/object
```

```bash
    gsutil rewrite -s coldline gs://mybucket/something.txt
```