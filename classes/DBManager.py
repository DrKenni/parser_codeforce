import requests
import psycopg2

site = 'https://codeforces.com/api/problemset.problems?lang=ru'


class Parser:

    @staticmethod
    def get_data(link):
        req = requests.get(link)
        req.encoding = 'utf-8'
        scr = req.text
        return print(scr)


Parser.get_data(site)


class DB_Manager:
    """Класс для работы с базой данных"""
    def __init__(self, params, name_db):
        self.params = params
        self.name_db = name_db

    def create_db(self):
        conn = psycopg2.connect(dbname="postgres", **self.params)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"DROP DATABASE IF EXISTS {self.name_db}")
        cursor.execute(f"CREATE DATABASE {self.name_db}")
        conn.close()
        print(f"База данных {self.name_db} успешно создана.")

    def create_tables(self) -> None:
        """Создает таблицы"""
        conn = psycopg2.connect(dbname=self.name_db, **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("""CREATE TABLE Task(
                       id SERIAL PRIMARY KEY,
                       contextId INT,
                       index VARCHAR(10) NOT NULL,
                       name VARCHAR(150) NOT NULL,
                       type VARCHAR(150) NOT NULL,
                       points INT,
                       rating INT,
                       tags VARCHAR(250)
                    )""")

        conn.close()
        print(f"Создание таблиц прошло успешно.")
