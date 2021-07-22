# Networking
- IP (Internet Protocol) Address
    - Unique identifer for a computer connected to the internet
    - a dotted quad ex... 123.222.32.4
    - Each section can hava a value from 0 - 255
    - Each quad is 1 byte
    - highest possible ip address value would be 11111111.11111111.11111111.11111111
        - For convience most IPs are written in decimal 255.255.255.255
- The Problem with IP v4 
    - In this system only about 4.2 billion unique identifiers exist
        - In the early 1980s when the system was created this was not problem
        - Now There are more computers then that could connect to the internet
        - IP v6 was invented to increase this number
- Subnets
    - A logical subspace of a network within a range of IPs
    - Why subnet?
        - **Performance**. Machines on the same subnet can communicate quickly with each without sending messages across the internet.
        - **Security**. Subnets have a single point of entry which can be used to filter incoming traffic.
        - **Organization**. You can apply some rule uniformally on machines in a subnet
    - Subnet mask
        - Are sent with the IP address to say what parts of the IP address it the network what is the host.
            - 11001001.00101010.10101010.10101111 IP address
            - 11111111.11111111.00000000.00000000 Subnet mask
                - same as 255.255.0.0
                - CIDR notation 201.42.170.175/16
            - Network: 11001001.00101010 is the network
            - Host: 10101010.10101111

- Classes Inter-Domain Routing CIDR
    - IP address are split into network and host
    - The CIDR notation lets you know what bits are reserved for the network and host(server)
    - 123.6.32.201/24
        - 123.6.32 is the network IP
        - 201 is the host IP
    - GCP does allow you increase the CIDR range on subnets
    - Google reserves 4 IPs per subnet
    - X.X.X.X/28
        - (32-28)<sub>remaining bits</sub> ^2 - 4 <sub>reserved IPs</sub> = 12 usable host IPs in this subnet
- Common ports
    - HTTP: 80
    - HTTPS: 443
    - SSH: 22
    - FTP: 20
    - SMTP: 25



- Premium Tier Routing
    - Cold potato
    - Traffic enters Google's network at location closest to the user
    - Faster and Google can optimize traffic flow
- Standard Tier Routing
    - Hot Potato
    - Traffic enters Google's network closes to the server
    - Traffic travels through the public internet jumping from location to location
    - Slower with more oppurtunties for failures or intercepts
- Reducing Latency
    - Position servers physically closer to the client
    - Light speed still takes time when it's across the planet
    - Cross Region Loadbalancing
        - Manages requests by splitting traffic to the correct server physically
- Unicast
    - There is only one IP address that can handle this request
- Anycast
    - There are multiple IP addresses that can handle this request. Pick closest one.
- Multicast
    - There are multiple IP addresses that can handle this request. Send it to all of them.
- OSI Open Systems Interconnnections
    - Layer 4 TCP/IP
        - TCP(Transport Control Protocol)
        - Transport layer
        - Send information in segments and chunks
        - Uses IP address to message other computers on the internet
    - Layer 7 Application Layer
        - HTTP and HTTPS
        - Routing with URL paths
- Domain Name System DNS

### VPC Virtul Private Cloud
- Software defined network SDN
- VPCs are global 
    - You can have a host project that owns the VPC and service projects can use that VPC
    - Routes
        - Instance level tags
    - **Firewall rules**
        - Filter/block traffic on a network
        - Restrictive by default
            - No traffic allowed in
        - Can be applied to 
            - All instances in the network
            - A service account
            - Network Tag
        - Can filter by
            - IP ranges
            - service account
            - source tags
        - Firewall rules can have priorities
            - The lower the number the higher the priority
            - 0 is highest
            - 65535 is lowest
            - Defaul trules have a priority of 65534 
- Subnets are regional
    - when networks are autocreated they create a subnet in each region

# Load Balancers
    - Load Balancers split traffic to different instances
    - HTTP(S) Load Balancer
        - External 
        - Handles HTTP and HTTPS requests
        - Treats every request as a new request
    - TCP Proxy Load Balancer
        - External or internal
        - Handles non HTTP or HTTPS TCP requests
    - SSL (Secure Socket layer) Proxy Load Balancer
        - Handles HTTP requests
        - Different from HTTPS load balancer as the SSL will connect a single user to a single instance
```bash
    gcloud compute target-pools add-instances my-vm-pool --instances vm1,vm4
    gcloud compute forwarding-rules create my-lb --port=80 --target-pool=my-vm-pool

    gcloud compute networks subnets expand-ip-range my-subnet --prefix-length 12
    
```

# Google Domains
- Register a Domain with Google Domains
- Private whois

# Cloud DNS
- Google's Domain Name Service
- Domain names are how humans can remember and get websites
    - google.com not 127.32.33.12
- There are a few root DNS servers in the world
    - These servers are a dictionary of domain names connected to IP addresses
- The process for client
    1. The client makes a request for cnn.com in the browser
    2. The browser makes a request to the nearest DNS server to see what IP is cnn.com
    3. The browser caches that information locally
    4. future requests from that browser for cnn.com go to the IP address
- The process for the website hoster
    1. Buy a domain name
    2. Add a record to the DNS root server connecting your domain to an IP
        - This is for A type records
    3. Set a time to live for the record
        - How often the root server will check your record to see that the IP has not changed
- 100% uptime

```bash
    gcloud dns records-set transaction start --zone=my-zone
    gcloud dns records-set transaction add 192.34.32.43 --name=awesome.com --ttl=300 --type=A --zone=my-zone

```


# Cloud Load Balancing
- Service for doing load balances
- Has a static IP
- However because of Google's network traffic is still directed to the nearest entry point to google's network

# Cloud CDN
- Cache data at different geographic locations all around the world
- Can reduce latency and reduce cost as there is less traffic being sent to the other side of the world

# Cloud Interconnect
- Connect external infrastracture to cloud resources

# Cloud Dedicated Interconnect
- Connect physically to a GCP VPC and your own data center

# CDN Interconnect
- Use a CDN that is not part of Google's CDN

# Cloud VPN
- Googles VPN service
- Allows you to securely send traffic to and from your network to Google's network

# Static IP
- Reserve static IPs and assign them to resources


# CLI commands

```bash
gcloud compute networks subnet describe {subnet-name} --region=central-us1
```