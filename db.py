from configparser import ConfigParser
from os import environ
from typing import Callable

config = ConfigParser()
config.read('.env.db')
config = config["ENV"]

import psycopg2

get_conn = lambda: psycopg2.connect(
    dbname=config["POSTGRES_DATABASE"],
    user=config["POSTGRES_USER"],
    password=config["POSTGRES_PASSWORD"],
    host=config["POSTGRES_HOST"],
)


def use_db(f: Callable):
    def wrapper(*args, **kwargs):
        conn = get_conn()
        cur = conn.cursor()

        req = f(cur, conn, *args, **kwargs)

        cur.close()
        conn.close()

        return req

    return wrapper


@use_db
def execute(cur: psycopg2._psycopg.cursor, conn: psycopg2._psycopg.connection, *args):
    cur.execute(*args)
    conn.commit()

@use_db
def executescript(cur: psycopg2._psycopg.cursor, conn: psycopg2._psycopg.connection, *args):
    cur.executescript(*args)
    conn.commit()


@use_db
def fetchone(cur: psycopg2._psycopg.cursor, _, *args):
    cur.execute(*args)
    return cur.fetchone()

@use_db
def fetchall(cur: psycopg2._psycopg.cursor, _, *args):
    cur.execute(*args)
    return cur.fetchall()
