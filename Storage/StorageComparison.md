# Types of Storage 
- Object Storage 
     - Store things in terms of objects/blobs
     - These objects are stored in buckets
     - Each Object is individually addressable
        - Usually via a URL
    - Access control can be fined tuned per object
    - Infintely scalable
- File Storage
    - Hierarchical system of files and directories
    - *NOT* stored on a specific VM
- Block Storage
    - Data is stored in **blocks**
    - Harddisks and SSDs
    - Blocks can be accesed directly
    - File systems are built on top of Block storage
- Cache
    - Data stored in memory
    - Very fast
    - Volatile
        - Data can be lost if system rebooted, application crashes etc...

|Service| Type Of Storage | Attached to an instance | latency | Data survives Instance Deletion |
|-|-|-|-|-|
|Persistent Disk | Block | No | milleseconds |Yes |
|Local Disk | Block | Yes | milleseconds | No |
| GCS | Object | No | milleseconds to seconds | Yes |
| Filestore | File | No | milleseconds | Yes |
| Memorystore | Cache | No | nanoseconds | No