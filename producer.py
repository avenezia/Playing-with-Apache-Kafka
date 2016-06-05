from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['u1401.ambari.apache.org:6667', 'u1402.ambari.apache.org:6667', 'u1403.ambari.apache.org:6667'])
future = producer.send('test', 'Hello Kafka')
record_metadata = future.get(timeout=10)
print record_metadata