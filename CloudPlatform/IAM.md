# Identity Access Management

# The 3 A's of Security
- Authentication
    - Is this person who they claim to be
- Authorization
    - Does this person have persmission 
- Auditing
    - Who did what when

### Overview
    - IAM is used to control who can do what in GCP
    - You should follow the least privellage principle
        - Assign the minimum privileages possible to achieve the job 

## Key Terminology
- **Resource**
    - Some service, IT infrastructure

    - Examples
        - Cloud Compute instance
        - Clud Function
        - SQL database
        - Kubernetes Cluster

- **Permission**
    - Enables a certain action
    - Service.Resource.Verb
```bash
    storage.buckets.get
    pubsub.topics.publish
```
- **Role**
    - A group of permissions
    - Primitive roles (In-built Project scope roles with broad permissions)
        - Viewer
            - View anything
        - Editor
            - view/edit anything
        - Owner
            - complete access including billing
    - Predefined roles
        - More specific roles
        - Usually for a certain feature or job (appengine.deployer has read and configuration access)
    - Custom role
        - custom role created for project
- **Member**
    - An entity that will use GCP resources
        - user
            - A person
        - serviceAccount
            - Some GCP Resource
        - group
            - A collection of users and/or serviceAccounts
                - developers@joespizza.com
                - authservers@joespizza.com
        - domain
            - Anyone with a specic email address domain
        - authenticatedUsers
            - Anyone with a GCP account
        - allUsers
            - Anyone on the internet
- **Policy**
    - A binding of role, member and scope 
    - Each Resource can have only 1 policies.
    - Policies can only grant permissions

# Scopes of a policies
- Organization 
    - Folder (optional)
        - Project 
            - Resource (Service account level)

### Service Accounts
- Service Accounts are the primary way of giving credentials to resources
- You can have GCP generate keys (reccomended)
- You can generate your own but GCP limits this to 10
    - Primarily just for key rotation
- A compute engine instance will have a default service account if not selected
    - You can delete the default service account

### Predefined roles
- 

```json
{
    "bindings":[
        {
            "role": "appengine.deployer",
            "members":[
                "user:adam.ranieri@revature.com",
                "group:devops@joespizza.com"
            ]
        }
    ]
}

```
```bash
    gcloud projects add-iam-policy-binding joespizza --member='user:test-user@gmail.com' --role='roles/editor'
```




- By Default Project resources cannot access each other

# Google Identity
- Provides identification for users without g-suite of google accounts

# Security Key Enforcement
- Multi Factor Authentication

# Cloud Identity Aware Proxy (IAP)
- Protect endpoints with identity verification
