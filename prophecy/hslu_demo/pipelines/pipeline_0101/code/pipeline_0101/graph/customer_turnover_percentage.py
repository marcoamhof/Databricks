from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *

def customer_turnover_percentage(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("CustomerID"), 
        col("CompanyName"), 
        col("Turnover"), 
        ((col("Turnover") / col("TotalDueSum")) * lit(100)).cast(DecimalType(18, 2)).alias("TurnoverPct")
    )
