from fastapi import FastAPI
import data.db
from data.helpers.commons import (get_all_distros, 
                                  get_distro_by_name, 
                                  get_all_desktops,
                                  get_desktop_by_name,
                                  get_all_kernels,
                                  get_kernel_by_name)
app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"OK": 200}

@app.get("/distros")
def get_distros():
    return get_all_distros(data.db.s)

@app.get("/distros/{distro_name}")
def get_distro(distro_name):
    return get_distro_by_name(data.db.s, distro_name)

@app.get("/desktops")
def get_distros():
    return get_all_desktops(data.db.s)

@app.get("/desktops/{desktop_name}")
def get_distro(desktop_name):
    return get_desktop_by_name(data.db.s, desktop_name)

@app.get("/kernels")
def get_distros():
    return get_all_kernels(data.db.s)

@app.get("/kernels/{kernel_name}")
def get_distro(kernel_name):
    return get_kernel_by_name(data.db.s, kernel_name)
