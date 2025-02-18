from confluent_kafka import Consumer
import time

#kafka broker configuration
conf = {'bootstrap.servers': 'localhost:9092',
        'group.id':'test_group1',
        'auto.offset.reset':'earliest'
        }

# create consumer instance

consumer= Consumer(conf)
topic = 'test_topic'

#suscribe to the topic
consumer.subscribe([topic])

print("Listening to messages for Group 1 consumer....")

try:
    while True:
        msg = consumer.poll(1.0)  # wait for message
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer Error: {msg.error()}")
            continue
        print(f" Consumer_group 1 , name is {msg.key()} value is {msg.value()} from partition : {msg.partition()}")
except:
    print("Shutting down consumer Group 1....")

finally:
    consumer.close()
