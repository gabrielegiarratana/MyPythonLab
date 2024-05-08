import pyspark
from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import pyspark.sql.functions as F


def get_dataframe(data):
    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", IntegerType(), True),
        ]
    )
    return spark.createDataFrame(data=data, schema=schema)


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark example").getOrCreate()

    data = [(1, 100), (2, 200), (3, 300), (4, 400)]

    update_data = [(1, 101), (4, 401), (5, 500)]  # updated record  # updated record

    df = get_dataframe(data)

    update_df = get_dataframe(update_data)

    upsert_df = (
        df.alias("old")
        .join(update_df.alias("new"), ["id"], "outer")
        .select("id", F.coalesce("new.value", "old.value").alias("value"))
    )

    upsert_df.orderBy("id").show(truncate=False)
