# Google Kubernetes Engine
- Was originally Google Contatiner Engine
    - the commands are gcloud containers
- GKE does not have IAM integration
    - Access must be done more manually
        - Keys, credetnial json etc..
- Depolyments do not encounter fatal errors.
    - The pods they control do
- GKE Reserves CPU and memory on nodes to run effectively
    - Memory Reserved starts at 25% for first 4 GB then scales down to 2% over 128 GB
    - CPU 6% for this first core scaling to 0.25% for cores 5 and up
- GKE monitors your cluster
    - Can notify you when certain conditions are met.
        - CPU utilization hits a certain point etc...

# Commands
- gcloud commands edit the cluster or create cluster


```bash
    gcloud container clusters create mycluster
```
```bash
    gcloud container clusters resize mycluster --node-pool default-pool --size 5 
```

```bash
    gcloud container clusters update mycluster --enable-autoscaling 
```

### Common Flags
- --num-nodes

# Google Container Registry
- Google's version of Dockerhub

```bash
    gcloud container images list
```
