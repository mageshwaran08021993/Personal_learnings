from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType, IntegerType

@udf(returnType=StringType())
def get_english_name(species):
    return species.split(" (")[0]

@udf(returnType=IntegerType())
def get_start_year(period):
    return int(period.split("-")[0].replace("(",""))

@udf(returnType=StringType())
def get_trend(annual_percentage_change):
    if annual_percentage_change < -3:
        return "strong decline"
    elif annual_percentage_change >= -3.00 and annual_percentage_change <= -0.50:
        return "weak decline"
    elif annual_percentage_change > -0.50 and annual_percentage_change < 0.50:
        return "no change"
    elif annual_percentage_change >= 0.50 and annual_percentage_change <= 3.00:
        return "weak increase"
    elif annual_percentage_change > 3.00:
        return "strong increase"
