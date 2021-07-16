
# gcloud vs gsutil
- most commands start with gcloud
- gsutil is for a cloud storage
    - gsutil is actually a python application

# login
```bash
    gcloud auth login
```

```bash
    gcloud auth list
```
# Set Project

```bash
    gcloud config set project myProject
```

# Get help
```bash
    gcloud help something
```

# Get IAM roles
```bash
    #gcloud project get-iam-policy {projectID}
    gcloud project get-iam-policy joespizza
```

# Add policy
```bash
    gcloud projects add-iam-policy-binding joespizza --member user:rickybobby@gmail.com --role roles/owner
```

# Get information
```bash
    #gcloud hierarchy,
    gcloud compute instances list
```
```bash
    # Get information on who is logged in this sdk and what project you are on
    gcloud config list
```

# Cloud Storage
- Use **gsutil** command
```bash
    # make bucket
    gsutil mb awesomebucket
```

# Billing
```bash
    gcloud beta billing
```

# Enabling a service
```bash
    gcloud services enable xyz.googleapis.com
    gcloud services enable xyz
```