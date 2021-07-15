# Compute Engine
- Virtual Machines/servers in the cloud
- Provide the most customizability of any computing service
- IP addresses are ephemeral and may be reassigned when an instance restarts
    - GCP caps you at 5 static IPs per account. You can request more.
- Compute Cloud uses disks for a hard drive
    - Can create snapshots of the disk
    - Can be configured automatically


# TidBits
- Startup scripts execute everytime you restart an instance
    - Meta-data startup script

# Retrieve meta data
```bash 
# must include header Metadata-Flavor: Google otherwise 403
curl http://metadata.google.internal/computeMetadata/v1/
```

# create instance template
```bash
glcoud compute instance-template create hello-template --source-instance=hello-server --source-instance-zone=us-central1-a
```
