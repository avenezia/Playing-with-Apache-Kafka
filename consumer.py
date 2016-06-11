from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer('test', bootstrap_servers=['u1401.ambari.apache.org:6667', 'u1402.ambari.apache.org:6667', 'u1403.ambari.apache.org:6667'])
for message in consumer:
    print message