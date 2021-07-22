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
- **least privellage principle**
    - Assign the minimum privileages possible to achieve the job 
- **seperation of duties**
    - A task should be split by multiple people to prevent fraud and errors
- **layers of defense**
    - Security should be redundant and done at every level


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
- **Identity**
    - An identity is an email address record that connects to a person, resource or group
    - An entity that will use GCP resources
        - user
            - A person
            - jane@joespizza.com
        - serviceAccount
            - Some GCP Resource
            - awesomeserver@joespizza.com
        - group
            - A collection of users and/or serviceAccounts
                - developers@joespizza.com
                - authservers@joespizza.com
        - domain
            - Anyone with a specic email address domain
            - @joespizza.com
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

**Access Scopes**
- Not direclty connected to scopes of policies
- legacy system of vms
- Scopes say what vms can do.
    - Both the scope and the service account must give access 

### Service Accounts
- Service account have a dual role
    - Sometimes they are an **Identity**
        - awesomeserver@joespizza.com is a vm that has certain roles 
    - Sometimes they are a **Resource**
        - kim@joedevtem.com can be granted an editor role to awesomeserver@joespizza.com w
        - Kim can now edit awesomeserver@joespizza.com service account
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

```bash
    gcloud projects get-iam-policy joespizza
```

```bash
    gcloud iam roles describe roles/appengine.serviceAgent
```

```bash
    gcloud iam roles create
```




- By Default Project resources cannot access each other

# Google Identity
- Provides identification for users without g-suite of google accounts

# Security Key Enforcement
- Multi Factor Authentication

# Cloud Identity Aware Proxy (IAP)
- Protect endpoints with identity verification
