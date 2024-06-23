"""GRIMORIO APIS"""
from datetime import datetime

from fastapi import APIRouter

from api.schemas import RegisterSchema, DeleteSchema
from api.docs import register_200, register_400, update_200, update_400, change_status_200, delete_200, get_grimorio_200, get_student_200
from dao.students import Student
from dao.magic import Magic
from dao.status import Status
from dao.grimorio import Grimorio

from errors.custom_error import SQLException
from utils.utils import get_trebol

router = APIRouter(tags=["magic academy"])

STATUS_REGISTER = "Registrado"
STATUS_UPDATE = "Actualizado"
STATUS_REJECTED = "Rechazado"
STATUS_ACCEPTED = "Aceptado"


@router.post(
    "/solicitud",
    summary="Register student request",
    responses={200: register_200, 400 : register_400},
)
async def register(register: RegisterSchema) -> dict:
    get_status = Status.retrivied_status_by_name(STATUS_REGISTER)
    if not get_status:
        return {"message": "status not found", "code": 400}
    get_magic = Magic.retrivied_magical_affinity_by_name(register.magical_affinity)
    if not get_magic:
        return {"message": "magical affinity not found", "code": 400}
    try:
        reg_student = Student.register_student(register.name,
                                               register.lastname,
                                               register.identidication,
                                               register.age, get_magic[0],
                                               get_status[0], datetime.now())
    except SQLException as ex:
        return {
            "message": "An error occurred while trying to save the student",
            "code": 400, "error": str(ex)
        }
    return {"message": "ok", "code": 200, "student": reg_student}

@router.put(
    "/solicitud/{student_id}",
    summary="Update student request",
    responses={200: update_200, 400: update_400},
)
async def update_student(student_id: int, register: RegisterSchema) -> dict:
    get_student = Student.retrivied_by_id(student_id)
    if not get_student:
        return {"message": "student not found", "code": 400}
    get_status = Status.retrivied_status_by_name(STATUS_UPDATE)
    if not get_status:
        return {"message": "status not found", "code": 400}
    get_magic = Magic.retrivied_magical_affinity_by_name(register.magical_affinity)
    if not get_magic:
        return {"message": "magical affinity not found", "code": 400}
    try:
        Student.update_student(int(student_id),
                               register.name,
                               register.lastname,
                               register.identidication,
                               register.age,
                               get_magic[0],
                               get_status[0],
                               datetime.now())
    except SQLException as ex:
        return {
            "message": "An error occurred while trying to save the student",
            "code": 400, "error": str(ex)
        }
    return {"message": "ok", "code": 200, "student": student_id}

@router.patch(
    "/solicitud/{student_id}/status",
    summary="Accept or reject student",
    responses={200: change_status_200, 400: update_400},
)
async def status_student(student_id: int, delete_data: DeleteSchema) -> dict:
    sys_date = datetime.now()
    canceled_status = Status.retrivied_status_by_name(STATUS_REJECTED)
    if not canceled_status:
        return {"message": "status rejected not found", "code": 400}
    get_student = Student.retrivied_by_id(student_id)
    if not get_student:
        return {"message": "student not found", "code": 400}
    if get_student[1]:
        return {"message": "student with asigned grimorio", "code": 400}
    if get_student[2] == canceled_status[0]:
        return {"message": "student with rejected status", "code": 400}
    if delete_data.approved is False:
        Student.update_student_status(student_id, canceled_status[0], sys_date)
        return {"message": "student rejected", "code": 200}
    get_status = Status.retrivied_status_by_name(STATUS_ACCEPTED)
    if not get_status:
        return {"message": "status not found", "code": 400}
    selected_grimorio = get_trebol()
    get_grimorio = Grimorio.retrivied_by_value(selected_grimorio)
    print(get_grimorio)
    if not get_grimorio:
        return {"message": f"grimorio with value {selected_grimorio} not found", "code": 400}
    Student.update_student_accept(student_id, get_status[0], get_grimorio[0], sys_date)
    return {"message": "accepted student",
            "code": 200, "student": student_id,
            "grimorio": get_grimorio[1],
            "rarity": get_grimorio[2]
        }

@router.get(
    "/solicitudes",
    summary="Get all students",
    responses={200: get_student_200},
)
async def get_students() -> dict:
    get_all = Student.get_all_students()
    return {"students": get_all}

@router.get(
    "/asignaciones",
    summary="Get students by grimorio",
    responses={200: get_grimorio_200},
)
async def get_grimorios() -> dict:
    get_all = Grimorio.get_count_students()
    return {"grimorios": get_all}

@router.delete(
    "/solicitud/{student_id}",
    summary="Delete students register",
    responses={200: delete_200, 400: update_400},
)
async def delete_student(student_id: int) -> dict:
    get_student = Student.retrivied_by_id(student_id)
    if not get_student:
        return {"message": "student not found", "code": 400}
    Student.delete_student(student_id)
    return {"message": "deleted", "code": 200, "student": student_id}