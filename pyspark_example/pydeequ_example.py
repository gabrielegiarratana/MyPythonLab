from pyspark.sql import SparkSession, Row
import pydeequ

if __name__ == "__main__":

    spark = (
        SparkSession.builder.config("spark.jars.packages", pydeequ.deequ_maven_coord)
        .config("spark.jars.excludes", pydeequ.f2j_maven_coord)
        .getOrCreate()
    )

    df = spark.sparkContext.parallelize(
        [Row(a="foo", b=1, c=5), Row(a="bar", b=2, c=6), Row(a="baz", b=3, c=None)]
    ).toDF()

    df.show()

    # Set up a PySpark session
    from pyspark.sql import SparkSession, Row
    import pydeequ

    spark = (
        SparkSession.builder.config("spark.jars.packages", pydeequ.deequ_maven_coord)
        .config("spark.jars.excludes", pydeequ.f2j_maven_coord)
        .getOrCreate()
    )

    df = spark.sparkContext.parallelize(
        [Row(a="foo", b=1, c=5), Row(a="bar", b=2, c=6), Row(a="baz", b=3, c=None)]
    ).toDF()

    # Analyzers

    from pydeequ.analyzers import *

    analysisResult = (
        AnalysisRunner(spark)
        .onData(df)
        .addAnalyzer(Size())
        .addAnalyzer(Completeness("b"))
        .run()
    )

    analysisResult_df = AnalyzerContext.successMetricsAsDataFrame(spark, analysisResult)
    analysisResult_df.show()

    # Profile
    from pydeequ.profiles import *

    result = ColumnProfilerRunner(spark).onData(df).run()

    for col, profile in result.profiles.items():
        print(profile)

    # Constraint Suggestions
    from pydeequ.suggestions import *

    suggestionResult = (
        ConstraintSuggestionRunner(spark).onData(df).addConstraintRule(DEFAULT()).run()
    )

    # Constraint Suggestions in JSON format
    print(suggestionResult)

    # Constraint Verification
    from pydeequ.checks import *
    from pydeequ.verification import *

    check = Check(spark, CheckLevel.Warning, "Review Check")

    checkResult = (
        VerificationSuite(spark)
        .onData(df)
        .addCheck(
            check.hasSize(lambda x: x >= 3)
            .hasMin("b", lambda x: x == 0)
            .isComplete("c")
            .isUnique("a")
            .isContainedIn("a", ["foo", "bar", "baz"])
            .isNonNegative("b")
        )
        .run()
    )

    checkResult_df = VerificationResult.checkResultsAsDataFrame(spark, checkResult)
    checkResult_df.show()

    # Repository
    from pydeequ.repository import *
    from pydeequ.analyzers import *

    metrics_file = FileSystemMetricsRepository.helper_metrics_file(
        spark, "metrics.json"
    )
    repository = FileSystemMetricsRepository(spark, metrics_file)
    key_tags = {"tag": "pydeequ hello world"}
    resultKey = ResultKey(spark, ResultKey.current_milli_time(), key_tags)

    analysisResult = (
        AnalysisRunner(spark)
        .onData(df)
        .addAnalyzer(ApproxCountDistinct("b"))
        .useRepository(repository)
        .saveOrAppendResult(resultKey)
        .run()
    )

    # Wrapping up
    spark.sparkContext._gateway.shutdown_callback_server()
    spark.stop()
