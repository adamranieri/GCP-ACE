# Compute Engine
- Virtual Machines/servers in the cloud
- Provide the most customizability of any computing service
- IP addresses are ephemeral and may be reassigned when an instance restarts
    - GCP caps you at 5 static IPs per account. You can request more.
- Compute Cloud uses disks for a hard drive
    - Can create snapshots of the disk
    - Can be configured automatically
- New Instance Creation Sequence
    1. A host machine will allocate space for a vm
        - The instance is in the *Provisioning* state
    2. After space is provisioned a network adaptor is configured for the instance
        - The instance is in the *Staging* state
    3. Boot the OS and get the metadata
        - The instance is in the *Running* state
    4. The startup script begins
        - Startup script can be set as a metadata tag
- Running an application on a compute engine
    - Applications can use the SDK on the computer engine
    - They can query the metadata of the instance


# Marketplace
- Previously called launcher
- Quickly get custom images 




# TidBits
- Startup scripts execute everytime you restart an instance
    - Meta-data startup script
- Service Accounts

# Retrieve meta data
- Meta data can be retrieved by making http requests
- The header Metadata-Flavor: Google
- Applications using the SDK on this compute engine will make requests to the meta data for authorization
```bash 
# must include header Metadata-Flavor: Google otherwise 403
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/
```

# create instance template
```bash
glcoud compute instance-template create hello-template --source-instance=hello-server --source-instance-zone=us-central1-a
```
