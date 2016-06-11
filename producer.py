from kafka import KafkaProducer
import datetime
import random
import time

producer = KafkaProducer(bootstrap_servers=['u1401.ambari.apache.org:6667', 'u1402.ambari.apache.org:6667', 'u1403.ambari.apache.org:6667'])
message_id = 0
while True:
    time.sleep(random.uniform(0, 3))
    future = producer.send('test', str(message_id) + "_" + datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
    message_id += 1
    print future.get(timeout=10)