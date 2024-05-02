import json
from kafka import KafkaProducer

# Kafka producer configurations
bootstrap_servers = "localhost:9092"
topic_name = "bankbranch"

# Create a Kafka producer with JSON serialization
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce messages to the "bankbranch" topic
producer.send(topic_name, {'atmid': 1, 'transid': 100})
producer.send(topic_name, {'atmid': 2, 'transid': 101})
producer.send(topic_name, {'atmid': 2, 'transid': 102})
producer.send(topic_name, {'atmid': 2, 'transid': 103})

# Close the producer when done
producer.close()
