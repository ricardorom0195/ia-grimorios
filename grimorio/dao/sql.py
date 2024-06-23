"""SQL CONECCTION"""

import os

import psycopg2

from errors.custom_error import SQLException

class SQL:
    """SQL CONECCTION CLASS"""
    __instance = None
    conn = None

    def __new__(cls):
        if SQL.__instance is None:
            SQL.__instance = object.__new__(cls)
        return SQL.__instance

    @classmethod
    def get_data(cls, data):
        return SQL(**data)

    @classmethod
    def init(cls):
        if not cls.conn:
            print("incia conexion sql")
            cls.conn = psycopg2.connect(
                host=os.environ.get('HOST_SQL'),
                port=os.environ.get('PORT_SQL'),
                database=os.environ.get('DATABASE_SQL'),
                user=os.environ.get('USER_SQL'),
                password=os.environ.get('PASSWORD_SQL'),
            )
            cls.conn.autocommit = False
            return SQL()
        else:
            return SQL()

    @classmethod
    def execute(cls, command, values=None):
        try:
            if not values:
                raise SQLException('empty values')
            cur = cls.conn.cursor()
            cur.execute(command, list(values.values()))
            resp = cur.fetchone()[0]
            cur.close()
            values['id'] = resp
            return values
        except psycopg2.errors.UniqueViolation as ex:
            print(f'error {ex}')
            cls.rollback()
            raise SQLException(str(ex))
        except Exception as ex:
            print(f'error {ex}')
            cls.rollback()
            # cls.conn.close()
            raise SQLException()

    @classmethod
    def save(cls, command, values=None):
        try:
            if not values:
                raise SQLException('empty values')
            cur = cls.conn.cursor()
            cur.execute(command, list(values.values()))
            cur.close()
        except psycopg2.errors.UniqueViolation as ex:
            print(f'error {ex}')
            cls.rollback()
            raise SQLException(str(ex))
        except Exception as ex:
            print(f'error {ex}')
            cls.rollback()
            # cls.close()
            raise SQLException()

    @classmethod
    def retrivied_data(cls, command, values=None):
        try:
            cur = cls.conn.cursor()
            if values:
                cur.execute(command, list(values.values()))
            else:
                cur.execute(command)
            rows = cur.fetchall()
            if rows:
                return rows
            else:
                return None
        except Exception as ex:
            print(f'error {ex}')
            # cls.conn.close()

    @classmethod
    def retrivied_all_wcolumnsname(cls, command, values=None):
        try:
            cur = cls.conn.cursor()

            if values:
                cur.execute(command, list(values.values()))
            else:
                cur.execute(command)

            rows = [x for x in cur]
            cols = [x[0] for x in cur.description]
            items = []
            for row in rows:
                item = {}
                for prop, val in zip(cols, row):
                    item[prop] = val
                items.append(item)

            if items:
                return items
            else:
                return None
        except Exception as ex:
            print(f'error {ex}')
            # cls.conn.close()

    @classmethod
    def commit(cls):
        if cls.conn:
            cls.conn.commit()

    @classmethod
    def rollback(cls):
        if cls.conn:
            cls.conn.rollback()

    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()
            cls.conn = None
