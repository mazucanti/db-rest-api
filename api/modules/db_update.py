import pandas as pd
import psycopg2
import os

def get_connection():
    conn = psycopg2(
        host='localhost',
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        database=os.environ['POSTGRES_DB']
    )
    return conn