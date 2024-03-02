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
def execute(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection, *args):
    cur.execute(*args)
    conn.commit()

@use_db
def executescript(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection, *args):
    cur.executescript(*args)
    conn.commit()


@use_db
def fetchone(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection, *args):
    return cur.execute(*args).fetchone()

@use_db
def fetchall(cur: psycopg2.extensions.cursor, conn: psycopg2.extensions.connection, *args):
    cur.execute(*args).fetchall()
