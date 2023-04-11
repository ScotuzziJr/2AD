import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from data.db import DataBaseConnection, DataBaseOperationsORM
from data.models import Desktop, Kernel, base

base_url = "https://distrowatch.com/table.php?distribution="
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)

db_conn = DataBaseConnection(base)
db = db_conn.create_connection()
s = db_conn.create_session(db)

db_orm = DataBaseOperationsORM(db, s, base)

# db_orm.recreate_database()

with open("distros.txt", "r") as f:
    distros = f.readlines()
    for distro in distros:
        browser.get(base_url + distro[:-1])

        xpath_name = "/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr[2]/td"
        name = browser.find_element(By.XPATH, xpath_name).text

        xpath_site_url = "/html/body/table[2]/tbody/tr/td[1]/table[2]/tbody/tr[3]/td"
        site_url = browser.find_element(By.XPATH, xpath_site_url).text

        xpath_info_ul = (
            "/html/body/table[2]/tbody/tr/td[1]/table[1]/tbody/tr[2]/td/div[2]/ul"
        )
        info_ul = browser.find_element(By.XPATH, xpath_info_ul)

        distro_data = info_ul.find_elements(By.TAG_NAME, "li")
        distro_data = list(map(lambda li: li.text.split(":"), distro_data))

        distro_data = list(map(lambda info: info[1].strip(), distro_data))

        distro_data.append(name)
        distro_data.append(site_url)

        print(distro_data)

        name = distro_data[8]
        origin = distro_data[2]
        based_on = list(map(lambda info: info.strip(), distro_data[1].split(",")))
        architecture = list(map(lambda info: info.strip(), distro_data[3].split(",")))
        desktop = list(map(lambda info: info.strip(), distro_data[4].split(",")))
        kernel = distro_data[0]
        category = list(map(lambda info: info.strip(), distro_data[5].split(",")))
        status = distro_data[6]
        website = distro_data[9]

        for d in desktop:
            if not s.query(Desktop).filter_by(name=d).first():
                db_orm.add_desktop(d)

        if not s.query(Kernel).filter_by(name=kernel).first():
            db_orm.add_kernel(kernel)

        payload_to_save_to_database = {
            "name": name,
            "origin": origin,
            "based_on": based_on[0],
            "architecture": architecture[0],
            "desktop": desktop[0],
            "kernel": kernel,
            "category": category[0],
            "status": status,
            "website": website,
        }

        db_orm.add_distro(payload_to_save_to_database)
    browser.close()
