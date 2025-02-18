# kafka-basics

start zookeeper: bin/zookeeper-server-start.sh config/zookeeper.properties
start kafka broker/server : bin/kafka-server-start.sh config/server.properties

create topic:  ./bin/kafka-topics.sh \
>  --create --topic test_topic \
> --bootstrap-server localhost:9092 \
> --partitions 3 \
> --replication-factor 1


zookeeper runs at 2181 , broker/server at 9092


within the files Producer.py creates the messages. Above we are creating a kafka topic (test_topic) with 3 partitions.
Why 3? Because I want to test different scenarios of consumers (below)

There are other three consumer files 1 , 1NEW and 2. Here Consumer1 and Consumer1_NEW is within the same consumer group. Hence the partitions will be distributed and messages will be sent as per the partition assigned to the consumer.
Consumer2 on the other hand, is within different consumer group (group2) and doen't have any other consumer within the group. Hence messages from all partitions of the topic will be accessible.

What more can be done here?
Adding encryption, SSL/authentication for the producer/consumer, etc (i don't have any idea yet). More will be done on it.
