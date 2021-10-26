# Databricks notebook source
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("DataFrame").getOrCreate()

# COMMAND ----------

data=spark.read.option("header",True).csv("/FileStore/tables/StudentData-2.csv")
data.show()
data.printSchema()

# COMMAND ----------

#Total Number Of Students
data.count()

# COMMAND ----------

#Number Of male and Female Students by each course
data.groupBy("gender","course").count().show()

# COMMAND ----------

#Total Marks acheived by each gender in each course
from pyspark.sql.functions import col,max,min,avg,sum,count
from pyspark.sql.types import IntegerType
data=data.withColumn("marks",col("marks").cast(IntegerType()))
data.groupBy("gender","course").agg(sum("marks")).show()

# COMMAND ----------

#Min marks Acheived in each course by age group
data.groupBy("age","course").agg(min("marks")).show()

# COMMAND ----------

#Max marks Acheived in each course by age group
data.groupBy("age","course").agg(max("marks")).show()

# COMMAND ----------




# COMMAND ----------




# COMMAND ----------


