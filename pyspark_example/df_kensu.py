import pyspark
from kensu.pyspark import init_kensu_spark
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import kensu.pyspark as py


# TODO


def get_dataframe(data):
    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", IntegerType(), True),
        ]
    )
    return spark.createDataFrame(data=data, schema=schema)


if __name__ == "__main__":
    app_name = "Spark example with Kensu"
    spark: SparkSession = (
        SparkSession.builder.config(
            "spark.driver.extraClassPath",
            "../resources/kensu-spark-collector-1.3.0_spark-3.2.1.jar",
        )
        .appName(app_name)
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("INFO")
    # Init Kensu
    init_kensu_spark(
        spark_session=spark,
        project_name="My first Kensu Project",
        shutdown_timeout_sec=10 * 60,
        process_name=app_name,
    )
    py.init_kensu_spark(pyspark)

    data = [(1, "Gabriele"), (2, "John"), (3, "Mary"), (4, "Claire")]

    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", StringType(), True),
        ]
    )
    df = spark.createDataFrame(data=data, schema=schema)

    df.orderBy("id").show(truncate=False)
