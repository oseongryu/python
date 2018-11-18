from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome('C:\\Temp\\chromedriver.exe')
browser.get("url")
browser.find_the_element_by_id("add_button").click()

try:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

    alert = browser.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")