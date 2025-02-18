from confluent_kafka import Producer
import time

# broker configuration
conf = {'bootstrap.servers': 'localhost:9092'}

#create producer instance
producer = Producer(conf)

#kafka topic
topic = 'test_topic'

def delivery_report(err,msg):
    """ callback for deliver reports"""
    if err:
        print(f"Message failed: {err}")
    else:
        print(f"Message delivery success \n Topic: {msg.topic()}\t partition: {msg.partition()}")

message = True
while (message!='STOP'):
    message = input("Enter the name , age, partition(0,1,2) with a space: ")
    
    if len(message.split(' ')) ==3:
        key, data, partition_num = message.split(' ')

        producer.produce(topic, key=str(key), value=data, partition =int(partition_num), callback=delivery_report)
        producer.flush()   
        time.sleep(1)
    else:
        print("Please enter correct values again.")

print("Closing Producer ...")