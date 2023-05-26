import csv
from sqlalchemy.sql import text
import re


def insert_csv_table(db, file_path, table):
    sql_base = (
        f"INSERT INTO public.{table}\n"
        "    VALUES"
    )
    with open(file_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        sql = batch_processing(db, sql_base, datareader)
        insert_batch(db, sql)


def batch_processing(db, sql_base, datareader):
    i = 0
    sql = sql_base
    for row in datareader:
        if i < 1000:
            sql = sql + f'{tuple(row)},\n'
            i+=1
        else:
            sql = sql + f'{tuple(row)};'
            insert_batch(db, sql)
            sql = sql_base
            i = 0
    sql = sql[:-2] + ';'
    return sql

def insert_batch(db, sql):
    sql = sql.replace("\'\'", "NULL")
    sql = sql.replace('\"', "\'")
    sql = re.sub(r"(\w+)'(\w+)", r"\1 \2", sql)
    with db.engine.connect() as conn:
        conn.execute(text(sql))
        conn.commit()
