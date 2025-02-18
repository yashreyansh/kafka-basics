from confluent_kafka import Consumer

conf = {
    'bootstrap.servers':'localhost:9092',
    'group.id': 'test_group2',
    'auto.offset.reset':'earliest'
}

consumer = Consumer(conf)

topic = 'test_topic'

consumer.subscribe([topic])

print(f"Consumer started.... Listening to {topic}")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg ==None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        print(f" Consumer_group : 2, name is {msg.key()} value is {msg.value()} from partition : {msg.partition()}")
        

except KeyboardInterrupt:
    print("Shutting Down consumer...")
finally:
    print(f"Closing Consumer from Group: 2 .......")
    consumer.close()
