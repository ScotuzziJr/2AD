from fastapi import FastAPI

from data.db import DataBaseConnection, DataBaseOperationsORM
from data.models import base

app = FastAPI()

db_conn = DataBaseConnection(base)
db = db_conn.create_connection()
s = db_conn.create_session(db)

db_orm = DataBaseOperationsORM(db, s, base)

db_orm.recreate_database()
db_orm.populate_db()


@app.get("/healthcheck")
def healthcheck():
    return {"OK": 200}


@app.get("/distros")
def get_distros():
    return db_orm.get_all_distros()


@app.get("/distros/{distro_name}")
def get_distro(distro_name):
    return db_orm.get_distro_by_name(distro_name)


@app.get("/desktops")
def get_desktops():
    return db_orm.get_all_desktops()


@app.get("/desktops/{desktop_name}")
def get_desktop(desktop_name):
    return db_orm.get_desktop_by_name(desktop_name)


@app.get("/kernels")
def get_kernels():
    return db_orm.get_all_kernels()


@app.get("/kernels/{kernel_name}")
def get_kernel(kernel_name):
    return db_orm.get_kernel_by_name(kernel_name)
