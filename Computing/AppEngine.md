
# App Engine
- App Engine is a PaaS
- App Engine has 4 components
    - Application
    - Service
    - Version
    - Instance
        - VM that runs a service
        - Resident: always up and running
        - Dynamic: Can be deleted or created via autoscaling
- An App Engine is a single application (only 1 per project)
    - 1 Application has many services
    - Each service can have many versions
        - A version is a unique combination of source code and an app.yaml
    - Each version runs on one or more instances
- You can host an application using  App Engine
    - It will automate deployment
    - It will use HTTP
    - It can do autoscaling
- App Engine has a default **projectid@app.spot** service account with Editor access in project
    - The url to appengine would be https://projectname.appspot.com
- Comes in two varieties
    - App Engine Standard
        - What most people want
        - Cheaper
        - Supports specific versions of runtime environments
            - Java
            - Node
            - Python
            - PHP
            - Ruby 
            - Go
        - Great elasticity
    - App Engine Flexible
        - More niche use
        - Can use containers
            - More expensive than cloud run but always running
        - Pricier
        - Can be customized for any runtime environment
        - Cannot scale as fast
        - Because the app runs in a container logging should be done to stdout or stderr and the logs will automatically be picked up
- App Engine can split incoming traffic in three ways
    - random
    - IP Address
    - GOOGAPPUID cookie (preferred)

- Main configuration file is an ***app.yaml*** stored with the project code
    - put in root directory
- [Examples](../examples)
```yaml
runtime: nodejs14
service: login

```
```yaml
env: flex # for containers
service: accounting
```
- Deployment notes
    - Your application ***MUST*** listen for a environment variable called PORT
    - For some apps host name must be 0.0.0.0
    - In *node* App Engine calls npm run start to begin the application


# Commands

### Create App
```bash
    gcloud app create --project=myprojectid
```

### Deploy App
```bash
    # execute in directory that has app.yaml
    gcloud app deploy
```

### Stop a version
```bash
    gcloud app versions stop authservicev1 shoppingservicev3
```

### routing traffic

```bash
    gcloud app services set-traffic authservice --splits authv3=.35 authv4=.66
    --migrate
    --split-by

```

### Important flags
- --version
- --project
- --no-promote
    - do not route traffic to this version