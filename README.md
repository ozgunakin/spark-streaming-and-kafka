# Spark Streaming and Kafka Integration

This is project includes a streaming data pipeline established using apache Kafka and Spark. Data will be sent to the HDFS after processed by spark streaming. It is assumed that there is continuous data flow from Twitter to Kafka.

## Architecture

![](.gitbook/assets/image.png)

## Step 1 - Download Proper Dependencies

External jar files should be downloaded to integrate Kafka and Spark. Versions of Kafka and Spark should be known for searching and downloading the right jar files. If the wrong files are downloaded, integrations will be failed. In this project, Spark-2.4.7 and Kafka-2.1.1 were used. You can find proper jar files in this repository for the integration of mentioned versions. For further information, you can visit; [https://spark.apache.org/docs/latest/streaming-kafka-0-10-integration.html](https://spark.apache.org/docs/latest/streaming-kafka-0-10-integration.html)

* [x] Download **spark-sql-kafka** jar for structured streaming from maven repository: [https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10\_2.12/2.4.7](https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10_2.12/2.4.7)
* [x] Download **kafka-clients** jar for structured streaming from maven repository: [https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients/2.1.1](https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients/2.1.1)
* [x] Download **spark-streaming-kafka** jar from maven repository: [https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10\_2.11/2.4.7](https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10_2.11/2.4.7)

You can put these files into a directory you select. Note the directory path to use later !!!

## Step 2 - Prepare Additional Directories

Spark streaming application needs spesific dire One of these will be used to store metadata and checkpoint files will be stored in the second one. Before run Spark Streaming code, you need to set up these directories and adjust proper permissions.

* [x] Create a project directory and go inside the directory.

```text
sudo mkdir my-streaming-project
cd my-streaming-project
```

* [x] Create a checkpoint directory inside the project directory.

```text
sudo mkdir checkpoint
```

## Step 3 - Prepare Spark Streaming Code

This pyspark code reads tweets from a Kafka topic and saves these data to HDFS.

* [x] After preparing your spark streaming code, save it as **spark-streaming.py**

```python
import pyspark.sql.functions as F
frompyspark.sql import SparkSession
frompyspark.streaming import StreamingContext
frompyspark.sql.types import *
frompyspark.sql.functionsimportfrom_json,col,to_json
import pyspark
frompyspark.sql.functionsimport col,
when,regexp_replace,from_unixtime
frompyspark.sql.functionsimportlit
import datetime
frompyspark.sql.functionsimport year, month, dayofmonth,hour

spark = SparkSession.builder\
.master("local")\
.appName("streamingAppOzgun")\
.config("spark.driver.cores", 1)\
.config("spark.executor.cores", 1)\
.config("spark.executor.memory", "1g")\
.config("spark.driver.memory", "1g")\
.config("spark.executor.instances", 1).getOrCreate()
sc = spark.sparkContext

schema=spark.read.json("/home/ubuntu/schema/twitterschema").schema
print(schema)

df = spark \
.readStream\
.format("kafka") \
.option("kafka.bootstrap.servers", "localhost:9092") \
.option("subscribe", "tweetTopic") \ #Kafka TopicName= tweetTopic
.option("failOnDataLoss","false")\
.load() \
.select(from_json(col("value").cast("string"), schema).alias("opc"))
df=df.select("opc.*")
df.printSchema()

query = df\
.writeStream\
.format("parquet") \
.option("checkpointLocation", "/home/ubuntu/my-streaming-project/checkpoint") \
.option("path", "&HADOOP_FILE_PATH/streamingOutput") \
.trigger(processingTime="10 seconds") \
.start()
query.awaitTermination()
```

## Step 4 - Submit Spark Streaming Code

* [x] Run your streaming code on bash. Do not forget to add jar files you downloaded at step 1.

```text
spark-submit --verbose --master local --jars /home/ubuntu/jars/spark-sql-kafka-0-10_2.11-2.4.7.jar,/home/ubuntu/jars/spark-streaming-kafka-0-10_2.11-2.4.7.jar,/home/ubuntu/jars/kafka-clients-2.1.1.jar /home/ubuntu/spark-code/spark-streaming.py
```

## Conclusion

Congratulations !! You have successfully integrated Kafka and Spark Streaming. 

