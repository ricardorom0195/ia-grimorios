"""Docs APIS Swagger responses."""

register_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "message": "ok",
                "code": 200,
                "student": {
                    "name": "Juan",
                    "lastname": "Perez",
                    "idt": "ggggff1ff",
                    "age": 22,
                    "magic": 3,
                    "status": 1,
                    "date": "2024-06-22T12:44:02.162298",
                    "id": 52
                }
            }
        }
    },
}

register_400 = {
    "description": "Caso erroneo",
    "content": {
        "application/json": {
            "example":{
                "message": "magical affinity not found",
                "code": 400
            }
        }
    },
}

update_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "message": "ok",
                "code": 200,
                "student": 1
            }
        }
    },
}

update_400 = {
    "description": "Caso erroneo",
    "content": {
        "application/json": {
            "example":{
                "message": "student not found",
                "code": 400
            }
        }
    },
}

change_status_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "message": "accepted student",
                "code": 200,
                "student": 2,
                "grimorio": "Trebol 2 hojas",
                "rarity": "Comun"
            }
        }
    },
}

delete_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "message": "deleted",
                "code": 200,
                "student": 1
            }
        }
    },
}

get_student_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "students": [
                    {
                        "id": 3,
                        "name": "TestUser",
                        "lastname": "TestLastName",
                        "age": 18,
                        "identification": "tu9ib57mgm",
                        "grimorio": None,
                        "magical_affinity": "Agua",
                        "status": "Registrado"
                    },
                    {
                        "id": 3,
                        "name": "User",
                        "lastname": "Lastname",
                        "age": 18,
                        "identification": "tu9ib57mgm",
                        "grimorio": "Fuego",
                        "magical_affinity": "Agua",
                        "status": "Aceptado"
                    }
                ]
            }
        }
    },
}

get_grimorio_200 = {
    "description": "Caso satisfactorio",
    "content": {
        "application/json": {
            "example":{
                "grimorios": [
                    {
                        "name": "Trebol 1 hoja",
                        "id": 1,
                        "total_students": 3
                    },
                    {
                        "name": "Trebol 2 hojas",
                        "id": 2,
                        "total_students": 1
                    },
                    {
                        "name": "Trebol 3 hojas",
                        "id": 3,
                        "total_students": 1
                    },
                    {
                        "name": "Trebol 4 hojas",
                        "id": 4,
                        "total_students": 1
                    },
                    {
                        "name": "Trebol 5 hojas",
                        "id": 5,
                        "total_students": 1
                    }
                ]
            }
        }
    },
}