# big-data-parcial3
Parcial final de bigdata
Guia:
# 1 Crear el entorno de kafka

Para esto se ejecuta en una terminal del EC2 el siguiente codigo:
bin/zookeeper-server-start.sh config/zookeeper.properties

Y en otra terminal del EC2 se ejecuta el siguiente codigo:
bin/kafka-server-start.sh config/server.properties

# 2 Creamos un tema donde guardaremos la información

Para esto se puede usar el siguiente codigo
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

# 3 Establecemos una conexion que permita importar y exportar los datos de la cola de kafka

Para esto se debe tener en cuenta que las versiones de kafka y pyspark deben coincidir tanto en el lado del servidor como en el del cliente
con el fin de evitar errores a la hora de pasar datos.

Despues editamos el archivo "config/connect-standalone.properties" habilitando el plugin de ruta de conexion
plugin.path=lib/connect-file-3.1.1.jar

# 4 Para establecer la conexion ejecutamos el siguiente codigo

bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties

# 5 Creamos el archivo consumer.py
Es el archivo que se encuentra en este repositorio con el nombre consumer.py

# 6 Creamos el archivo producer.py
Es el archivo que se encuentra en este repositorio con el nombre producer.py

# 7 Ejecutamos ambos archivos .py(consumer.py, producer.py)
Mandamos la información en formato csv del archivo SPY_TICK_TRADE.csv

# 8 Creamos un cluster en EMR de AWS
Dentro del cluster debemos instalar pyspark con el siguiente codigo:
pip install pyspark

# 9 Creamos el archivo consumer2.py
Es el archivo que se encuentra en la carpeta EMR de este repositorio con el nombre de consumer2.py

# 10 Enviamos data con el siguiente codigo al consumer2.py

nc -lk 9999

# 11 Ejecutamos el consumer2.py con el siguiente codigo

/bin/spark-submit consumer2.py localhost 9999

(En este proyecto se debia tener un productor de kafka compartido entre el EC2 y el EMR pero no se pudo debido a incompatibilidades entre versiones de las dos instancias. ademas no se pudo subir los archivos en formato csv porque no hubo errore con el timestamp y el withWaterMark del writerstream)
