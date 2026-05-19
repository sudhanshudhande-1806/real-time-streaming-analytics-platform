from pyspark.sql.functions import *

def apply_transformations(df):

    transformed_df = df \
        .filter(col("amount") > 0) \
        .filter(col("city").isNotNull()) \
        .dropDuplicates()

    return transformed_df