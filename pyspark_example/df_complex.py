from pyspark.sql.functions import col, regexp_replace

from pyspark.sql import SparkSession, Row, Column
from pyspark.sql.functions import sum, max


def remove_comma(str_with_comma: str):
    return str_with_comma.replace(",", "")


if __name__ == "__main__":

    spark = SparkSession.builder.appName("Spark API vs SQL example").getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    #########################
    # Using pyspark API
    #########################

    # Reading a CSV file
    source_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load("../resources/input/most_streamed_spotify_songs_2024.csv")
        .repartitionByRange("Artist")  # Creates partitions during the read
    )
    source_df.cache()

    # 1) Filter
    df = source_df.filter(source_df["Explicit Track"] == 0)

    # 2) Clean
    df = df.withColumn(
        "Spotify Streams", regexp_replace(col("Spotify Streams"), ",", "")
    )  # removing commas

    # 3) Cast
    print(f"Schema before cast: {df.schema}")
    df = df.withColumn("Spotify Streams", col("Spotify Streams").cast("long"))
    print(f"Schema after cast: {df.schema}")

    # 4) Group data by a column and perform aggregation
    df = df.groupBy("Artist").agg(
        sum("Spotify Streams").alias("sum_streams"),
        max("Spotify Popularity").alias("max_popularity"),
    )

    # 5) Writing in parquet format
    df.write.mode("overwrite").parquet(
        "../resources/most_streamed_spotify_songs_2024_api_parquet"
    )
    # NB: You can use both write.parquet or write.format("parquet")

    df.show(truncate=False)  # don't use show in real code ;)

    df.write.mode("overwrite").format("json").save(
        "../resources/output/most_streamed_spotify_songs_2024_api_json"
    )

    #########################
    # Using Spark SQL API
    #########################

    source_df.createOrReplaceTempView("mytable")
    count = source_df.count()
    print(count)
    df2 = spark.sql(
        """
    SELECT ARTIST, 
    sum (
        CAST(replace(`Spotify Streams`,",","") AS LONG)
        ) as sum_streams, max(`Spotify Popularity`) as max_popularity
    FROM mytable
    WHERE `Explicit Track` = 0
    GROUP BY ARTIST    
    """
    )

    print(df2.count())
    df2.show(truncate=False)  # don't use show in real code ;)
    df2.repartition(10).write.mode("overwrite").parquet(
        "../resources/output/most_streamed_spotify_songs_2024_sql_parquet"
    )
