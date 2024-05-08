from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import col

df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])


def cast_all_to_int(input_df):
    return input_df.select([col(col_name).cast("int") for col_name in input_df.columns])


def sort_columns_asc(input_df):
    return input_df.select(*sorted(input_df.columns))


def add_n(input_df, n):
    return input_df.select([(col(col_name) + n).alias(col_name)
                            for col_name in input_df.columns])


if __name__ == "__main__":

    print("Original dataframe")
    df.show()

    print("Dataframe after chaining transformations")
    (df
     .transform(cast_all_to_int)
     .transform(sort_columns_asc)
     .transform(add_n, 100)
     .show())
