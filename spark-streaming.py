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
