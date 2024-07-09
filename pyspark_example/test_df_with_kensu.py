import pyspark_example
from pyspark_example.sql import SparkSession, Row
from pyspark_example.sql.types import StructType, StructField, StringType, IntegerType
import pyspark_example.sql.functions as F
from kensu.utils.kensu_provider import KensuProvider

import kensu.pyspark as py


# TODO

process_name = "Spark example with Kensu"


def get_dataframe(data):
    schema = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("value", IntegerType(), True),
        ]
    )
    return spark.createDataFrame(data=data, schema=schema)


if __name__ == "__main__":
    K = KensuProvider().initKensu(allow_reinit=True, process_name=process_name)
    spark = SparkSession.builder.appName(process_name).getOrCreate()
    py.init_kensu_spark(pyspark_example)

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
