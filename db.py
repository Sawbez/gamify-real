from configparser import ConfigParser

import psycopg2

config = ConfigParser()
config.read('.env.db')
config = config["ENV"]

conn = psycopg2.connect(
    dbname=config["POSTGRES_DATABASE"],
    user=config["POSTGRES_USER"],
    password=config["POSTGRES_PASSWORD"],
    host=config["POSTGRES_HOST"],
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
def fetchone(cur, _, *args):
    return cur.execute(*args).fetchone()


@use_db
def fetchall(cur, conn, *args):
    return cur.execute(*args).fetchall()
