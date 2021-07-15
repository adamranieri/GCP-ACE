# Pod
- Smallest atomic unit of computing in a cluster.
- Consists of one to many containers
    - Most pods run only a single container
    - Only containers that are very tightly coupled are put in the same pod
        - This is an advanced use case

# Service
- Exposes pods
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
    - **Deployment** or ReplicaSet
        - For managing **stateless** pods
        - Kubernetes docs says to use Deployment unless you have a specific reason to use ReplicaSet
    - StatefulSet
        - For managing pods that have **persistent volumes**
    - DaemonSet
        - For managing pods that must run on a **specic node**
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



```bash
    kubectl expose deployment hello-app --type LoadBalancer --port 80 --targetPort 8080

```

```bash
    kubectl delete pods <pod>
```