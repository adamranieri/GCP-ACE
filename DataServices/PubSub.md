# Cloud Pub/Sub
- Infinitely scalable messaging system for ingestion
- Global service
- A **Topic**  is essentially a queue for messages
- A **Publisher** creates messages to be put in a topic
- A **Subsciber** conssumes messages from a topic
- Great for asynchronus workloads and as shock absorber
- Decouples applications and is a great "glue" service
- 10MB max per message
- Messages are stored for 7 days but no Dead Letter Queue
    - DLQ is a topic that is for unprocessable messages
- Push Mode
    - Topic recieves a message and sends it to subscribers 
    - Done over HTPPS
    - Slow Start means pus/sub will slowly ramp up deliveries as it gets back successes
- Pull Mode
    - Subscribers while poll the topic ever x seconds to get pending messages
    - Subscribers must acknowledge that a message has been handled before it disappears from the topic.
    - Can get messages in batches or long polling
- Pay for data volume

```bash
    gcloud pubsub topics create my-topic
    gcloud pubsub subscriptions create --topic my-topic my-subscription 

    gcloud pubsub topics publish my-topic --message "Hi, everybody!"
    gcloud public subscriptions pull --auto-ack my-subscription

```