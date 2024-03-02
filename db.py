from dotenv import load_dotenv
load_dotenv()
from os import environ

import psycopg2

conn = psycopg2.connect(
    dbname=environ["POSTGRES_DATABASE"],
    user=environ["POSTGRES_USER"],
    password=environ["POSTGRES_PASSWORD"],
    host=environ["POSTGRES_HOST"],
)


def use_db(f):
    def wrapper(*args, **kwargs):
        cur = conn.cursor()
        req = f(cur, conn, *args, **kwargs)
        cur.close()
        conn.close()

        return req

    return wrapper


@use_db
def execute(cur, conn, *args):
    cur.execute(*args)
    conn.commit()

@use_db
def executescript(cur, conn, *args):
    cur.executescript(*args)
    conn.commit()


@use_db
def fetchone(cur, conn, *args):
    return cur.execute(*args).fetchone()

@use_db
def fetchall(cur, conn, *args):
    cur.execute(*args).fetchall()
