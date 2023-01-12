from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as t


def main():
    # 1 create spark session
    spark = SparkSession.builder.getOrCreate()

    # EXTRACT
    # read data
    df = spark.read.format("csv").option("header", "true").load(
        "/Users/macbook/PycharmProjects/pyspark_local/data/cars.csv")
    # check read data
    # df.show(5)

    # TRANSFORM

    output = (
        df
        # считаем по каждому производителю
        .groupBy("manufacturer_name")
        .agg(
            # первая метрика - количество авто
            F.count("manufacturer_name").alias("count"),
            # вторая метрика  - средний год выпуска автомобилей
            F.round(F.avg("year_produced")).cast(t.IntegerType()).alias("avg_year"),
            # третья метрика - минимальная цена
            F.min("price_usd").alias("min_price"),
            # четвертая метрика - максимальная цена
            F.max("price_usd").alias("max_price")
        )

    )

    # output.show(6)

    # LOAD

    output.coalesce(1).write.mode("overwrite").format("csv").option("header", "true").save(
        "/Users/macbook/PycharmProjects/pyspark_local/data/cars_result_csv1.csv")


main()
