# Datastore
- NoSQL database
- Designed for more OLTP
    - for smaller web apps
- Pay for
    - Data stored
    - IO operations
- Use GQL (Google Query Language)
    - like SQL

```bash
    gcloud datastore export namespaces='(default)' gs://my-backup-bucket
    gcloud datstore import gs://my-backup-bucket.overall_export_metadata
    
```

### Firestore
- Newer version of Datastore
    - Part of Firebase