import csv


def insert_csv_table(db, file_path, table):
    sql_base = (
        f"INSERT INTO public.{table}\n"
        "    VALUES"
    )
    with open(file_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        sql = batch_processing(sql_base, datareader)
        db.engine.execute(sql)


def batch_processing(db, sql_base, datareader):
    i = 0
    sql = sql_base
    for row in datareader:
        if i < 1000:
            sql = sql + f'{tuple(row)},\n'
        else:
            sql = sql + f'{tuple(row)};'
            db.engine.execute(sql)
            sql = sql_base
            i = 0
    sql = sql[:-2] + ';'
    return sql
