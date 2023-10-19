from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *

def turnover_by_customer(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("CustomerID"), col("CompanyName"))

    return df1.agg(sum(col("Turnover")).alias("Turnover"))
