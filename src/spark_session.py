import os
import sys

from pyspark.sql import SparkSession


def get_spark(app_name: str = "series-spark", master: str = "local[*]") -> SparkSession:
    # O Spark abre os workers Python como processos separados e resolve o
    # interpretador pelo PATH, não pelo venv ativo. Fixar no mesmo
    # interpretador do driver evita mismatch de versão (Py4JJavaError).
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    spark = SparkSession.builder.master(master).appName(app_name).getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark
