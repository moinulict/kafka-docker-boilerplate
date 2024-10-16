
# Apache Kafka & Zookeeper Setup with Docker Compose

This repository provides an easy way to set up Apache Kafka and Zookeeper using Docker Compose. Kafka is a distributed streaming platform used for building real-time data pipelines and streaming applications, while Zookeeper is used for coordinating distributed systems.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to set up Kafka and Zookeeper on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/kafka-docker.git
cd kafka-docker
```

### 2. Create a Docker Compose File

Ensure the `docker-compose.yml` file contains the following:

```yaml
version: '3'
services:

  kafka:
    image: 'bitnami/kafka:latest'
    ports:
      - '9094:9094'
    environment:
      - KAFKA_CFG_NODE_ID=0
      - KAFKA_CFG_CONTROLLER_BROKER_ID=0
      - KAFKA_CFG_PROCESS_ROLES=controller,broker
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093,EXTERNAL://:9094
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092,EXTERNAL://localhost:9094
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,EXTERNAL:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=0@kafka:9093
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
  kafka-ui:
    image: 'provectuslabs/kafka-ui:latest'
    ports:
      - '5050:8080'
    depends_on:
      - kafka
    environment:
      - KAFKA_CLUSTERS_0_NAME=local
      - KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=kafka:9092
```

### 3. Start Kafka and UI

Run the following command to start Kafka and Zookeeper:

```bash
docker-compose up -d
```

### 4. Verify the Setup

Check if Kafka and Zookeeper containers are running:

```bash
docker-compose ps
```

---

## Kafka UI

[Visit Kafka GUI](https://localhost:5050)


### 3. **Viewing Kafka Logs**

View the logs for Kafka to troubleshoot issues:

```bash
docker-compose logs kafka
```

---

## Stopping and Removing Kafka and Zookeeper

### 1. **Stop Services**

To stop Kafka and Zookeeper:

```bash
docker-compose down
```

### 2. **Remove Persistent Data (Optional)**

If you want to remove the volumes and persistent data, use the `-v` flag:

```bash
docker-compose down -v
```

---

## Additional Resources

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Kafka Docker Images](https://hub.docker.com/r/confluentinc/cp-kafka/)

---

Now you have a quick setup for running Kafka and Zookeeper using Docker Compose along with useful commands to manage your Kafka cluster.
