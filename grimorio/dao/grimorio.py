"""GRIMORIO DB QUERIES"""

from dao.sql import SQL

class Grimorio:
    """GRIMORIO QUERY CLASS"""
    @classmethod
    def retrivied_by_value(cls, value):
        data = {
            'val': value
        }
        query = """select id, name, description from magia.grimorio where value = %s;"""
        result = SQL.retrivied_data(query,data)
        if result:
            return result[0]
        return None

    @classmethod
    def get_count_students(cls):
        query = """
                SELECT g.name, g.id, COUNT(s.grimorio) AS total_students
                FROM magia.grimorio g 
                JOIN magia.students s ON g.id = s.grimorio 
                GROUP BY g.id
                ORDER BY g.value ASC;
                """
        result = SQL.retrivied_all_wcolumnsname(query)
        if result:
            return result
        return []
