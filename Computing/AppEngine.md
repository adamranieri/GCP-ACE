# App Engine
- App Engine is a PaaS
- An App Engine is a single application
    - 1 Application has many services
    - Each service can have many versions
    - Each version runs on one or more instances
- You can host an application using  App Engine
    - It will automate deployment
    - It will use HTTP
    - It can do autoscaling
- App Engine has a default projectid@app.spot service account with Editor access in project
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

- Main configuration file is an app.yaml stored with the project code
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