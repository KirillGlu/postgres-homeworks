"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def add_customers_data():
    """Достает данные из csv файла и заполняет таблицу в базе данных"""
    with open('north_data/customers_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host='localhost', database='north', user='postgres', password='ghjcnjnfr') as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (row["customer_id"], row["company_name"], row["contact_name"]))

        cur.close()

def add_employess_data():
    """Достает данные из csv файла и заполняет таблицу в базе данных"""
    with open('north_data/employees_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host='localhost', database='north', user='postgres', password='ghjcnjnfr') as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (
                    row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))

        cur.close()

def add_orders_data():
    """Достает данные из csv файла и заполняет таблицу в базе данных"""
    with open('north_data/orders_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with psycopg2.connect(host='localhost', database='north', user='postgres', password='ghjcnjnfr') as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (
                    row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))

        cur.close()
