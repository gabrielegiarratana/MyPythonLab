import pyspark_example
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark example").getOrCreate()

    data = [(1, 100), (2, 200), (3, 300), (4, 400)]

    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", IntegerType(), True),
        ]
    )
    df = spark.createDataFrame(data=data, schema=schema)

    df.orderBy("id").show(truncate=False)
