from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *

def customer_order_join(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.CustomerID") == col("in1.CustomerID")), "inner")\
        .select(col("in0.CustomerID").alias("CustomerID"), col("in0.CompanyName").alias("CompanyName"), col("in1.TotalDue").alias("Turnover"))
