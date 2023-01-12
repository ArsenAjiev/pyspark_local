# Установка Pyspark локально из pip

## Предварительные требования

1. Python 3.6+

2. Установленная Java/OpenJDK версии 11 или выше.

   Проверить установку из терминала (Linux/macOs):

   ```bash
   java -version

   openjdk version "15.0.1" 2020-10-20
   OpenJDK Runtime Environment (build 15.0.1+9)
   OpenJDK 64-Bit Server VM (build 15.0.1+9, mixed mode, sharing)
   ```

## Установка Apache Spark

1. Делаем виртуальное окружение Python:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Активируем окружение:

   ```bash
   # Linux, macOs
   source venv/bin/activate

   # Windows
   venv\Scripts\activate.bat
   ```

   [Официальная инструкция](https://docs.python.org/3/library/venv.html) по активации окружения.

3. Ставим pyspark из `pip`:

   ```bash
   (venv) pip install pyspark
   ```



# Запуск Spark из Docker

## Предварительные требования

Установленный Docker.

## Установка Spark

Будем использовать образ [Jupyter notebooks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html) с установленным Apache Spark.

Запускаем контейнер в интерактивном режиме:

```bash
docker run -it -p 8888:8888 -p 4040:4040 -v $(pwd):/home/jovyan/work jupyter/pyspark-notebook
```

Остановка контейнера по CTRL + C.


# Запуск Spark в ноутбуках Google Collab

## Установка и запуск Apache Spark в облаке

1. Заходим на https://colab.research.google.com/
2. Выбираем вкладку GitHub и вставляем ссылку на стартовый ноутбук с нужным кодом:

```
https://github.com/oleg-agapov/getting-started-with-pyspark-ru/blob/master/practice-1/notebooks/google_collab_pyspark.ipynb
```

3. Вверху справа нажимаем Connect чтобы запустить окружение
4. Выполняем инструкции из ноутбука чтобы установить PySpark

Для своих целей не обязательно клонировать ноутбук, можно просто установить пакет `pyspark` и начать работать.