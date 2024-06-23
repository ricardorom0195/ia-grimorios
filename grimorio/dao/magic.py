"""MAGICAL AFFINITY DB QUERIES"""

from dao.sql import SQL

class Magic:
    """MAGICAL AFFINITY QUERY CLASS"""
    @classmethod
    def retrivied_magical_affinity_by_name(cls, name):
        data = {
            'name': name
        }
        query = """select id, name from magia.magical_affinity where name = %s;"""
        result = SQL.retrivied_data(query,data)
        if result:
            return result[0]
        return None
