# Compute Engine
- Virtual Machines/servers in the cloud
- Provide the most customizability of any computing service
- IP addresses are ephemeral and may be reassigned when an instance restarts
    - GCP caps you at 5 static IPs per account. You can request more.
- Compute Cloud uses disks for a hard drive
    - Can create snapshots of the disk
        - Snapshots work like version control and track changes to data to minimize size
        - Snapshot v1:100gb, Snapshot v2:105gb = 105 total gbs stored
            - 100 gbs from the originial 5 gbs from the changes
    - Can be configured automatically
- New Instance Creation Sequence
    0. A service account will be created or must already exist
    1. A host machine will allocate space for a vm
        - The instance is in the *Provisioning* state
    2. After space is provisioned a network adaptor is configured for the instance
        - The instance is in the *Staging* state
    3. Boot the OS and get the metadata
        - The instance is in the *Running* state
    4. gcloud command to start the instance is complete
    5. The startup script begins
        - Startup script can be set as a metadata tag
         
- Running an application on a compute engine
    - Applications can use the SDK on the computer engine
    - They can query the metadata of the instance

- Shield VMs
    - VMs can be protected from boot and kernel injection hacks
    - VMs can verify that boot disk integrity and OS is not compromised
# Images
- A format for quickly creating VMs
- It is images NOT disks used for instance templates
- can be created from 4 sources
    - Disk
    - Snapshot
    - Cloud Storage file
    - Another Image

# Instance Group
- A group of instances managed as a single entity
- Any command issued to an instance group is issued to all vms in the group
- Managed Instance group
    - All vms are of the same type and configuration
    - Must be created from a instance-template
- Unmanaged Instance group
    - VMs of different types and configurations are added to to the instance group
    - Usually for retroactivly creating a instance group of existing servers

### Administartion and Managing
- Use labels and descriptions
- Common or repeated tasks should be done via gcloud and scripts
    - Scripts and version control should be used to keep a record of configurations and why
- Console should be used for ad hoc administartion
- Use instance groups for auto-scaling
- Use preemptible VMs if possible
- Use snapshots to create backups and promote resusability


# Marketplace (Cloud Launcher)
- Previously called Launcher
- Quickly get custom images 
```yaml
resources:
- type: compute.v1.instance
  name: awesome-vm
```
```bash
    gcloud deployment-manager deployments create quickstart-deployment --config config.yaml
```

# TidBits
- Startup scripts execute everytime you restart an instance
    - Meta-data startup script
- Service Accounts

# Create an instance
```bash
    gcloud compute instances create --machine-type=n1-standard-8 awsesomeserver
```
### Common flags for creating instance
- --boot-disk-size
- --boot-disk-type
- --labels
- --machine-type
- --premptible
- --zone
- --async
    - gets info associated with start up
    - return immediately without waiting for it to finish


# Stop
```bash
    gcloud compute instances stop awsesomeserver
```

# Delete
```bash
    gcloud compute instances delete awsesomeserver
```


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
glcoud compute instance-templates create hello-template --source-instance=hello-server --source-instance-zone=us-central1-a
```

# Disks
```bash
    gcloud compute disks
```

# Snapshots
```bash
    gcloud compute snapshots
```

# Images
```bash
    gcloud compute images
```

# Instance Groups
```bash
    gcloud compute instance-groups
```

# Instance Templates
```bash
    gcloud compute instance-templates
```

```bash
    gcloud compute networks create my-vpc --subnet-mode=auto

    gcloud compute firewall-rules create
    gcloud compute firewall-rules create express-app –-network devnet –-allow tcp:3000
    gcloud compute shared-vpc 
    # you can applay a single vpc to multiple projects or folders
    
```
