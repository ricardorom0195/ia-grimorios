"""STUDENT STATUS DB QUERIES"""

from dao.sql import SQL

class Status:
    """STUDENT STATUS QUERY CLASS"""
    @classmethod
    def retrivied_status_by_name(cls, name):
        data = {
            'name': name
        }
        query = """select id, name from magia.student_status where name = %s;"""
        result = SQL.retrivied_data(query,data)
        if result:
            return result[0]
        return None
