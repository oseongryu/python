from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)
driver.maxmize_window()
driver.get("https://www.naver.com")

driver.find_element(By.CSS_SELECTOR, '#id')
id.click()

pyperclip.copy('')
pyautogui.hotkey('ctrl', "v")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#pw')
id.click()
id.send_keys('')
