"""STUDENTS DB QUERIES"""

from dao.sql import SQL

class Student:
    """STUDENT QUERY CLASS"""
    @classmethod
    def register_student(cls, name, lastname, idt, age, magic, status, date):
        data = {
            "name": name,
            "lastname": lastname,
            "idt": idt,
            "age": age,
            "magic": magic,
            "status": status,
            "date": date
        }
        query = """
            INSERT INTO magia.students(name, lastname, identification, age,
            magical_affinity, status, creation)
	        VALUES (%s, %s, %s, %s, %s, %s, %s) returning id;"""

        result = SQL.execute(query,data)
        SQL.commit()
        if result:
            return result
        return None

    @classmethod
    def update_student(cls, student_id, name, lastname, idt, age, magic, status, date):
        data = {
            "name": name,
            "lastname": lastname,
            "idt": idt,
            "age": age,
            "magic": magic,
            "date": date,
            "status": status,
            "id": student_id
        }
        query = """
            update magia.students set name = %s, lastname = %s, identification = %s,
            age = %s, magical_affinity = %s, last_update = %s, status = %s
	        where id = %s"""

        SQL.save(query,data)
        SQL.commit()

    @classmethod
    def retrivied_by_id(cls, student_id):
        data = {
            'id': student_id
        }
        query = """select id, grimorio, status from magia.students where id = %s;"""
        result = SQL.retrivied_data(query,data)
        if result:
            return result[0]
        return None

    @classmethod
    def update_student_status(cls, student_id, status, date):
        data = {
            "date": date,
            "status": status,
            "id": student_id
        }
        query = """
            update magia.students set last_update = %s, status = %s
	        where id = %s"""

        SQL.save(query,data)
        SQL.commit()

    @classmethod
    def update_student_accept(cls, student_id, status, grimorio, date):
        data = {
            "date": date,
            "status": status,
            "grimorio": grimorio,
            "id": student_id
        }
        query = """
            update magia.students set last_update = %s, status = %s,
            grimorio = %s where id = %s"""
        SQL.save(query,data)
        SQL.commit()

    @classmethod
    def get_all_students(cls):
        query = """
                select s.id, s.name, s.lastname, s.age, s.identification,
                gr.name as grimorio, ma.name as magical_affinity, ss.name as status
	            from magia.students s
	            left join magia.grimorio gr on gr.id = s.grimorio
	            left join magia.magical_affinity ma on ma.id = s.magical_affinity 
	            left join magia.student_status ss on ss.id = s.status;

                """
        result = SQL.retrivied_all_wcolumnsname(query)
        if result:
            return result
        return []

    @classmethod
    def delete_student(cls, student_id):
        data = {'id': student_id}
        SQL.save('delete from magia.students where id = %s', data)
