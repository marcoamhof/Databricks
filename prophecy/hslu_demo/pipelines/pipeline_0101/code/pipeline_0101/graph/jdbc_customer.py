from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *

def jdbc_customer(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("jdbc")\
        .option("url", "jdbc:sqlserver://sqlalzero.database.windows.net:1433;database=Adventureworks")\
        .option("user", "hsluStudent")\
        .option("password", "6300!Zug")\
        .option("dbtable", "SalesLT.Customer")\
        .option("pushDownPredicate", True)\
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver")\
        .load()
