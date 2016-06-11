from kafka import KafkaConsumer, TopicPartition

topic_name = "test"
consumer = KafkaConsumer(bootstrap_servers=['u1401.ambari.apache.org:6667', 'u1402.ambari.apache.org:6667', 'u1403.ambari.apache.org:6667'])
partitions = [TopicPartition(topic_name, partition) for partition in consumer.partitions_for_topic(topic_name) if partition < 5]
consumer.assign(partitions)
consumer.seek_to_beginning()
for message in consumer:
    print message