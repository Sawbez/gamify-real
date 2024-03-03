from configparser import ConfigParser
from dataclasses import asdict, dataclass
from os import environ
from typing import Callable, List, Optional, Type, TypeVar

import psycopg2
from psycopg2.extras import DictCursor

# Select correct configuration in prod
if environ.get("POSTGRES_DATABASE"):
    dbname = environ["POSTGRES_DATABASE"]
    user = environ["POSTGRES_USER"]
    password = environ["POSTGRES_PASSWORD"]
    host = environ["POSTGRES_HOST"]
else:
    config = ConfigParser()
    config.read(".env.db")
    config = config["ENV"]

    dbname = config["POSTGRES_DATABASE"]
    user = config["POSTGRES_USER"]
    password = config["POSTGRES_PASSWORD"]
    host = config["POSTGRES_HOST"]

T = TypeVar("T")  # Type variable for data class conversion


def get_conn():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        # cursor_factory=DictCursor,  # Use DictCursor to get rows as dictionaries
    )


def use_db(f: Callable) -> Callable:
    def wrapper(*args, dtype: Optional[T] = None, **kwargs):
        conn = get_conn()
        cur = conn.cursor()

        req = f(cur, conn, *args, **kwargs)

        if dtype and req:  # Convert result to data class instance(s) if applicable
            if isinstance(req, list):
                return [dtype(*row) for row in req]  # For fetchall
            return dtype(*req)  # For fetchone

        cur.close()
        conn.close()

        return req

    return wrapper


@use_db
def execute(cur: psycopg2._psycopg.cursor, conn: psycopg2._psycopg.connection, *args):
    cur.execute(*args)
    conn.commit()


@use_db
def fetchone(cur: psycopg2._psycopg.cursor, _, *args, **kwargs):
    cur.execute(*args)
    return cur.fetchone()


@use_db
def fetchall(cur: psycopg2._psycopg.cursor, _, *args, **kwargs):
    cur.execute(*args)
    return cur.fetchall()
