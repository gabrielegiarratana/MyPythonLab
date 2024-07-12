from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark example").getOrCreate()

    data = [(1, "Gabriele"), (2, "John"), (3, "Mary"), (4, "Claire")]

    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", StringType(), True),
        ]
    )
    df = spark.createDataFrame(data=data, schema=schema)

    df.orderBy("id").show(truncate=False)
