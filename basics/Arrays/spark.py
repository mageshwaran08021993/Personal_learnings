from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from solution.udfs import get_english_name, get_start_year, get_trend
from pyspark.sql import functions as f


class BirdsETLJob:
    input_path = 'data/input/birds.csv'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[1]")
                                          .appName("BirdsETLJob")
                                          .getOrCreate())

    def extract(self):
        input_schema = StructType([StructField("Species", StringType()),
                                   StructField("Category", StringType()),
                                   StructField("Period", StringType()),
                                   StructField("Annual percentage change", DoubleType())
                                   ])
        return self.spark_session.read.csv(self.input_path, header=True, schema=input_schema)

    def transform(self, df):
        # df.show(3)
        df_transform = df.withColumn("species", get_english_name(f.col("Species"))).withColumn("category", f.col("Category")).withColumn("collected_from_year", get_start_year(f.col("Period"))).withColumn("annual_percentage_change", f.col("Annual percentage change")).withColumn("trend", get_trend(f.col("Annual percentage change")))
        return df_transform.select("species", "category", "collected_from_year", "annual_percentage_change", "trend")

    def run(self):
        return self.transform(self.extract())
