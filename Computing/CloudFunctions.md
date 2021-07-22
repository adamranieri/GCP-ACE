# Cloud Function
- Run a code snippet in response to an event
    - Events include
        - HTTP request
            - GET, POST, PUT, DELETE
        - pub/sub
        - Cloud Storage
            - finalize (file finished uploading)
            - delete
            - archive
            - metadataUpdate
        - Firebase
        - logging
- NOT suitable for long running processing 
    - default is 1 minute
- NOT ideal for synchronous workloads
- Every function runs in its own environment
- Only supports some languages
    - node.js
    - Python
    - Go
    - Java
- Serverless FaaS (Functions as a service)
    - Very scalable
    - Great for applications that have very variable traffic
    - Acting as glue code to connect things together
- Every function gets its own HTTP endpoint


```bash
    gcloud functions deploy myfunction --runtime python27 --trigger-resource mybucket --trigger-event google.storage.object.ginalize
```
