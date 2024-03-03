from configparser import ConfigParser
from os import environ
from typing import Callable, Type, TypeVar, List
from dataclasses import dataclass, asdict
import psycopg2
from psycopg2.extras import DictCursor

config = ConfigParser()
config.read('.env.db')
config = config["ENV"]

T = TypeVar('T')  # Type variable for data class conversion

def get_conn():
    return psycopg2.connect(
        dbname=config["POSTGRES_DATABASE"],
        user=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],
        host=config["POSTGRES_HOST"],
        cursor_factory=DictCursor  # Use DictCursor to get rows as dictionaries
    )

def use_db(f: Callable):
    def wrapper(*args, data_class: Type[T] = None, **kwargs):  # Optional data_class argument
        conn = get_conn()
        cur = conn.cursor()

        req = f(cur, conn, *args, **kwargs)

        if data_class and req:  # Convert result to data class instance(s) if applicable
            if isinstance(req, list):
                return [data_class(**dict(row)) for row in req]  # For fetchall
            return data_class(**dict(req))  # For fetchone

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
