# Cluster
- A collection of nodes controlled by kubernetes
- A cluster has a master node that is the effective brain and command center of the cluster

# Node
- A VM (Physical computer if on premise) that is in a cluster
- A node runs an agent/software called **kubelet** which connects it the master node

# Controller
- Manages a pod(s)
- **ReplicaSet** is responsible for how many instances of a pod there are
- Eviction
    - Kubernetes shutting down a pod
- Preemption
    - Kubenetes evicts a Pod because resouces are needed for a higher priority pod

# Pod
- Smallest atomic unit of computing in a cluster
    - A self contained running process
    - A house for an application 
- Consists of one to many containers
    - Most pods run only a single container
    - Only containers that are very tightly coupled are put in the same pod
        - This is an advanced use case    
- Pod Statuses
    - Pending
        - Pod is downloading images
    - Running
    - Completed
        - Gracefully terminated
    - Failed
        - Fatal Error
    - Unknown
        - Cannot be reached
- Pods should be ephemeral and created or destroyed as needed
- Pods run as if they their own self-isolated VM
    - You can don't worry about port conlficts etc...
- A pod runs on a node


# Service
- Exposes pods to the outside intenet or to other pods
- The goal is to decouple reliance on a particular pod
- Pods in the cluster are not reachable from outside the cluster
- Services must be used to allows pods access to other pods or to the outside internet
- Service Types
    - NodePort
        - Exposes a pod(s) for access within a cluster
    - LoadBalancer
        - Offered by some cloud providers
        - Creates an external IP that can be used to expose a pod(s)

# Volume
- Decouple storage and persistence from the pod
    - Pods are ephemeral being created and destroyed as needed
    - Data in a pod is *NOT* persisted
- A Persistent Volume is a Kubenrenetes abstraction
    - Kubernetes does not magically have storage resources when you make a volume
    - There must be actual infrastructure somewhere
    - Volume Access Modes
        - RWO Read Write Once
            - Only a single pod can claim and use this volume
        - ROM Read Only Many
            - Many pods can *read* this volume
        - RWM Read Write Many
            - Many pods can claim and use this volume
    - Retention Policy
        - Says what to do with the volume when there are no claims
            - Retain
                - Volume persists
            - Delete
                - Volume is deleted from the cluster
- **Pesistent Volume Claim**
    - Volumes are not useable without a claim
    - A claim is seprate resource
    - It is like a voucher granting the ability to use a Persistent Volume


# Workload
- Manages a group of pods
- Types of Workloads
    - **Deployment** 
        - A released version of application code
        - Kubernetes docs recommend Deployment unless you have a specific reason to use ReplicaSet
            - A deployment is a "higher level concept"
            - The amount of replicas is *part of* a deployment just like what version of the container image to is *part of* the deployement
        - Deployment can be in one of three states
            - Progressing
                - In the process of deploying
            - Completed
                - Successfully running
            - Failed
                - Fatal error while deploying
    - StatefulSet
        - For managing pods that have stateful aspects like session handling
    - DaemonSet
        - For managing pods that must run on a **specfic node** or one pod on each node
    - Job and CronJob
        - For pods that that runs **until complete**
        - Example a pod that reads a database to create a report it sends to a bucket

# Ingress
- Serves as the entrypoint to a cluster
- Having an external LoadBalancer service for each group of pods needless exposes every service
    - It can also very expensive
    - You might want to control all traffic and do things like check headers do auth or create a unified path
- Ingresses by themselves do not do anything
    - They require an **Ingress Controller** to work
    - Nginx is an example

# Quick cheat sheet

- **kubectl get** - list resources
- **kubectl describe** - show detailed information about a resource
- **kubectl logs** - print the logs from a container in a pod
- **kubectl exec** - execute a command on a container in a pod





```bash
    kubectl describe pods mypodname
```

```bash
    kubectl delete pods <pod>
```

### Create a deployment
```bash
    kubectl run hello-app --image=awesome-app --port=8080
```
### Deployment Actions (modifies a running deployment)
```bash
    kubectl scale deployment hello-app --replicas=5 
```
```bash
    kubectl expose deployment hello-app --type LoadBalancer --port 80 --targetPort 8080
```
```bash
    kubectl auto-scale deployment hello-app --min 2 --max 5 --cpu-percent 75
```


