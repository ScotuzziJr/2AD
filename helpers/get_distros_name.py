from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Firefox()

browser.get("https://distrowatch.com/")

xpath_dropdown_distros = "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/select[1]"
dropdown_distros = browser.find_element(By.XPATH, xpath_dropdown_distros)

sleep(3)

distros = Select(dropdown_distros)

with open("distros.txt", "w") as f:
    for distro in distros.options:
        f.write(f'{distro.get_attribute("value")}\n')
        print(distro.get_attribute("value"))

browser.close()
