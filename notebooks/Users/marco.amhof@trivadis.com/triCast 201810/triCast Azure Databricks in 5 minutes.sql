-- Databricks notebook source
-- MAGIC %md
-- MAGIC <img src="https://www.trivadis.com/sites/all/themes/custom/img/trivadis-logo.svg"/>
-- MAGIC 
-- MAGIC # triCast Demo Azure Databricks in 5 minutes

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Create a quickstart cluster
-- MAGIC 
-- MAGIC 1. In the sidebar, right-click the **Clusters** button and open the link in a new window.
-- MAGIC 1. On the Clusters page, click **Create Cluster**.
-- MAGIC 1. Name the cluster **QuickstartDemo**.
-- MAGIC 1. In the Databricks Runtime Version drop-down, select **4.2 (includes Apache Spark 2.3.1, Scala 11)**.
-- MAGIC 1. Click **Create Cluster**.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Demo
-- MAGIC 
-- MAGIC - Display folder with databricks sample datasts
-- MAGIC - create a table (airports) from a tab delimited file (airport-codes-na.txt)
-- MAGIC - Display airports content
-- MAGIC - Query airports: 
-- MAGIC    - count airports by contry and state
-- MAGIC    - compare airport count (US and CAN)

-- COMMAND ----------

-- MAGIC %scala
-- MAGIC display(dbutils.fs.ls("/databricks-datasets/"))

-- COMMAND ----------

-- MAGIC %scala
-- MAGIC display(dbutils.fs.ls("/databricks-datasets/flights"))

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## Create a table from a tab delimited file (airport-codes-na.txt)

-- COMMAND ----------

DROP TABLE IF EXISTS airports;

CREATE TABLE airports
  USING csv
  OPTIONS (path "/databricks-datasets/flights/airport-codes-na.txt", header "true", delimiter "\t")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Display airport content

-- COMMAND ----------

SELECT COUNT(*) FROM airports

-- COMMAND ----------

SELECT * FROM airports

-- COMMAND ----------

SELECT Country, State, COUNT(*) AS AirportCount FROM airports GROUP BY Country, State ORDER BY COUNT(*) DESC

-- COMMAND ----------

SELECT Country, COUNT(*) AS AirportCount FROM airports GROUP BY Country ORDER BY COUNT(*) DESC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Convert the table to a chart
-- MAGIC 
-- MAGIC Under the table, click the bar chart <img src="http://docs.databricks.com/_static/images/notebooks/chart-button.png"/></a> icon. 

-- COMMAND ----------

-- MAGIC %md 
-- MAGIC ## Repeat the same operations using Python DataFrame API. 
-- MAGIC This is a SQL notebook.
-- MAGIC By default command statements are passed to a SQL interpreter. 
-- MAGIC To pass command statements to a Python interpreter, 
-- MAGIC include the `%python` magic command.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Create a DataFrame from tab delimited file

-- COMMAND ----------

-- MAGIC %python
-- MAGIC 
-- MAGIC airports = sqlContext.read.format("csv") \
-- MAGIC   .options(header="true", inferSchema="true", delimiter="\t") \
-- MAGIC   .load("/databricks-datasets/flights/airport-codes-na.txt")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query airports DataFrame
-- MAGIC - count airports by contry and state
-- MAGIC - compare airport count (US and CAN) 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from pyspark.sql.functions import count
-- MAGIC 
-- MAGIC airportsByCountry = airports.select("Country").groupBy("Country").agg(count("*").alias("AirportCount"))
-- MAGIC 
-- MAGIC display(airportsByCountry.sort("AirportCount", ascending=False))

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from pyspark.sql.functions import count
-- MAGIC 
-- MAGIC airportsByCountryAndState = airports.select("Country", "State").groupBy("Country", "State").agg(count("*").alias("AirportCount"))
-- MAGIC 
-- MAGIC display(airportsByCountryAndState.sort("AirportCount", ascending=False))