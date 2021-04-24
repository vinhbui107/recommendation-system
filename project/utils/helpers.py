#!/usr/bin/env python3
from decouple import config
import psycopg2


def connect_db():
    try:
        # PostgreSQL Database credentials loaded from the .env file
        DB_NAME = config("DB_NAME")
        DB_USER = config("DB_USER")
        DB_PASSWORD = config("DB_PASSWORD")
        DB_HOST = config("DB_HOST")
        DB_PORT = config("DB_PORT")

        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        return conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        return False
