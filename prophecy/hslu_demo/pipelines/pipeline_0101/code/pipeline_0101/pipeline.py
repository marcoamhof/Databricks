from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pipeline_0101.config.ConfigStore import *
from pipeline_0101.udfs.UDFs import *
from prophecy.utils import *
from pipeline_0101.graph import *

def pipeline(spark: SparkSession) -> None:
    df_jdbc_customer = jdbc_customer(spark)
    df_jdbc_salesorderheader = jdbc_salesorderheader(spark)
    df_customer_order_join = customer_order_join(spark, df_jdbc_customer, df_jdbc_salesorderheader)
    df_turnover_by_customer = turnover_by_customer(spark, df_customer_order_join)
    df_by_turnover_desc = by_turnover_desc(spark, df_turnover_by_customer)
    df_reformatted_turnover = reformatted_turnover(spark, df_by_turnover_desc)
    df_total_due_sum = total_due_sum(spark, df_jdbc_salesorderheader)
    jdbc_customer_report_extended(spark, df_reformatted_turnover)
    df_join_all = join_all(spark, df_total_due_sum, df_turnover_by_customer)
    df_customer_turnover_percentage = customer_turnover_percentage(spark, df_join_all)
    jdbc_output_customer_report_extended(spark, df_customer_turnover_percentage)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline_0101")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pipeline_0101", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pipeline_0101")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
