from kafka import KafkaConsumer

# Kafka consumer configurations
bootstrap_servers = "localhost:9092"
topic_name = "bankbranch"

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    value_deserializer=lambda v: v.decode("utf-8")
)

# Consume and print messages from the "bankbranch" topic
for msg in consumer:
    print(msg.value)

# Close the consumer when done
consumer.close()
