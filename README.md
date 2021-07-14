# Spark Streaming and Kafka Integration

This is project includes a streaming data pipeline established using apache Kafka and Spark. Data will be sent to the HDFS after processed by spark streaming.

## Architecture

![](.gitbook/assets/image.png)

## Step 1 - Download Proper Dependencies

External jar files should be downloaded to integrate Kafka and Spark. Versions of Kafka and Spark should be known for searching and downloading the right jar files. If the wrong files are downloaded, integrations will be failed. In this project, Spark-2.4.7 and Kafka-2.1.1 were used. You can find proper jar files in this repository for the integration of mentioned versions. For further information, you can visit; [https://spark.apache.org/docs/latest/streaming-kafka-0-10-integration.html](https://spark.apache.org/docs/latest/streaming-kafka-0-10-integration.html)

* [x] Download **spark-sql-kafka** jar for structured streaming from maven repository: [https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10\_2.12/2.4.7](https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10_2.12/2.4.7)
* [x] Download **kafka-clients** jar for structured streaming from maven repository: [https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients/2.1.1](https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients/2.1.1)
* [x] Download **spark-streaming-kafka** jar from maven repository: [https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10\_2.11/2.4.7](https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10_2.11/2.4.7)

You can put these files into a directory you select. Note the directory path to use later !!!

## Step 2 - Prepare Additional Directories

Spark streaming application needs two additional directories. One of these will be used to store metadata and checkpoint files will be stored in the second one. Before run Spark Streaming code, you need to set up these directories and adjust proper permissions.

* [x] Create a project directory and go inside the directory.

```text
sudo mkdir my-streaming-project
cd my-streaming-project
```

* [x] Create checkpoint and metadata directories inside the project directory.

```text
sudo mkdir checkpoint
sudo mkdir metadata
```







