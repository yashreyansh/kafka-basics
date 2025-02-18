from confluent_kafka import Consumer
import time

conf = {
    'bootstrap.servers' : 'localhost:9092',
    'group.id':'test_group1',
    'auto.offset.reset':'earliest'
}

consumer = Consumer(conf)
topic = 'test_topic'

consumer.subscribe([topic])

print("Group 1 (NEW) consumer started...")

try:
    while True:
        msg =  consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()} ....")
            continue
        print(f" Consumer_group1 (NEW), name is {msg.key()} value is {msg.value()} from partition : {msg.partition()}")
except:
    print("Shutting down group 1 (NEW) consumer...")
finally:
    consumer.close()