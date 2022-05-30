from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('quickstart-events', value=b'14856000,1406400,100,P,F,0')
producer.flush()