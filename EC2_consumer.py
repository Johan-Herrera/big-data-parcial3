  GNU nano 6.2                                                                                   consumer.py                                                                                            
from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events')
valor_maximo=1410500
valor_minimo=1400500
for message in consumer:
    c=0
    price_txt=""
    for i in range(len(message.value.decode('utf-8'))):
        if message.value.decode('utf-8')[i]==",":
            c=c+1
        if c==1 and message.value.decode('utf-8')[i]!=",":
            price_txt=price_txt+message.value.decode('utf-8')[i]
    if int(price_txt)<valor_minimo:
        print("ALERTA: El precio está por debajo del valor minimo establecido")
        print("Precio actual= "+price_txt+" | Valor minimo= "+str(valor_minimo))
    if int(price_txt)>valor_maximo:
        print("ALERTA: El precio está por encima del valor maximo establecido")
        print("Precio actual= "+price_txt+" | Valor maximo= "+str(valor_maximo))
    print (message.value.decode('utf-8'))