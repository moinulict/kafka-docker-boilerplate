from kazoo.client import KazooClient
from kafka import KafkaProducer, KafkaConsumer
import time

# Configure the topic name
topic_name = 'test-kafka'

# Zookeeper Connection Check
def check_zookeeper():
    # Create a client connection to Zookeeper
    zk = KazooClient(hosts='localhost:2181')
    zk.start()

    # Check the status of Zookeeper
    if zk.exists("/"):
        print("Zookeeper is running and reachable.")
    else:
        print("Could not connect to Zookeeper.")

    # Optional: Print Zookeeper node information
    zk_server_stat = zk.command(b"stat")  # Send the command as bytes
    print("Zookeeper Server Stat:", zk_server_stat)

    # Stop the client connection
    zk.stop()

# Function to produce messages
def produce_message():
    # Create a producer instance
    producer = KafkaProducer(bootstrap_servers='localhost:29092')

    # Produce a message
    message = b'Hello Kafka!'  # Messages should be bytes
    producer.send(topic_name, message)

    # Block until all messages are sent
    producer.flush()
    print("Message produced:", message.decode('utf-8'))

# Function to consume messages
def consume_message():
    # Create a consumer instance
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers='localhost:9094',
        #auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
    )

    print("Consuming messages from topic:", topic_name)
    for message in consumer:
        print("Message consumed:", message.value.decode('utf-8'))
        break  # Consume only one message and exit

if __name__ == '__main__':
    # Step 1: Check Zookeeper status
    #check_zookeeper()

    # Step 2: Produce and consume messages
    #produce_message()
    #time.sleep(2)  # Add a delay to ensure the message is produced before consuming
    consume_message()
