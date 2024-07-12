from enum import Enum

from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame


class StatsType(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


def calculate_stats(stats_type: StatsType = StatsType.LOW):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if (
                (stats_type == StatsType.LOW)
                or (stats_type == StatsType.MEDIUM)
                or (stats_type == StatsType.HIGH)
            ):
                print(f"Count: {result.count()}")
            if stats_type == StatsType.MEDIUM:
                print(f"Showing 5 rows of sampled data:")
                result.sample(0.1).show(n=5)
            if stats_type == StatsType.HIGH:
                print(f"Showing data:")
                result.show(n=10000)

        return wrapper

    return decorator


# Define a Spark function decorated with checkpoint_result
@calculate_stats(stats_type=StatsType.HIGH)  # process_df = calc_stats(process_df)
def process_df(read_options: dict, read_path: str) -> DataFrame:
    df_in = spark.read.options(**read_options).csv(read_path).select("Artist")
    df_out = df_in.where("Artist like 'A%'")
    df_out.write.mode("overwrite").parquet("my_parquet")
    return df_out


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark example").getOrCreate()
    read_opts: dict = {"inferSchema": "true", "header": "true"}

    process_df(
        read_opts, read_path="../resources/input/most_streamed_spotify_songs_2024.csv"
    )
