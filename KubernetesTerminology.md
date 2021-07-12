# Pod
- Smallest atomic unit of computing resources in a cluster.
- Consists of one to many containers
    - Most pods run only a single container
    - Only containers that are very tighly coupled are put in the same pod
        - This is an advanced use case

# Workload
- Manages a group of pods
- Types of Workloads
    - Deployment or ReplicaSet
        - For managing **stateless** pods
        - Kubernetes docs says to use Deployment unless you have a specific reason to use ReplicaSet
    - StatefulSet
        - For managing pods that have **persistent volumes**
    - DaemonSet
        - For managing pods that must run on a **specic node**
    - Job and CronJob
        - For pods that that runs **until complete**
        - Example a pod that reads a database to create a report it sends to a bucket


```bash
kubectl expose deployment hello-app --type LoadBalancer --port 80 --targetPort 8080

```