
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType, LongType


spark = SparkSession.builder.config("spark.jars", "/tmp/mssql-jdbc-12.4.1.jre8.jar").getOrCreate()

schema = StructType() \
    .add("timestamp", StringType()) \
    .add("open", FloatType()) \
    .add("high", FloatType()) \
    .add("low", FloatType()) \
    .add("close", FloatType()) \
    .add("volume", LongType())

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "10.128.0.2:9092") \
    .option("subscribe", "stock-data") \
    .option("startingOffsets", "latest") \
    .load()

parsed_df = kafka_df.selectExpr("CAST(value AS STRING) AS json_str") \
    .select(from_json(col("json_str"), schema).alias("data")) \
    .select("data.*")

def write_to_sql(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://ANANT;databaseName=Spark-pipeline") \
        .option("dbtable", "dbo.stock_data") \
        .option("user", "Anant2005") \ 
        .option("password", "Anant@2005") \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .mode("append") \
        .save()

query = parsed_df.writeStream \
    .outputMode("append") \
    .foreachBatch(write_to_sql) \
    .option("checkpointLocation", "/tmp/stock-data-checkpoint") \
    .start()

query.awaitTermination()
