from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *

def reformatted_turnover(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("CustomerID"), col("CompanyName"), col("Turnover").cast(DecimalType(18, 2)).alias("Turnover"))
