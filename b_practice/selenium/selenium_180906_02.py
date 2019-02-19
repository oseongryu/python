from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('C:\\Temp\\chromedriver.exe')
driver.implicitly_wait(10)

# 사이트 주소 입력
driver.get('http://abc3149.com/index.php')


lists_id = ['15','20','yesy']
lists_pw = ['15','20']


# #
# f_id = open("C:\\Users\\lst\\Desktop\\id.txt", 'r')
# while True:
#     line_id = f_id.readline()
#     if not line_id: break
#     # print(line_id)
#     lists_id.append(line_id.rstrip().lstrip())
# f_id.close()
#
#
# f_pw = open("C:\\Users\\lst\\Desktop\\pw.txt", 'r')
# while True:
#     line_pw = f_pw.readline()
#     if not line_pw: break
#     # print(line_pw)
#     lists_pw.append(line_pw.rstrip().lstrip())
# f_pw.close()


try:
    for list_id in lists_id:
        for list_pw in lists_pw:
            driver.find_element_by_id('userid').send_keys(list_id)
            driver.find_element_by_id('userpw').send_keys(list_pw)
            time.sleep(4)

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






# 로그인 버튼을 눌러주자.
# driver.find_element_by_xpath('//*[@id="loginField"]/fieldset/input').is_enabled()

# driver.find_element_by_xpath("//form[@class='LoginForm']/fieldset/input").send_keys(Keys.ENTER)
# driver.find_element_by_xpath("//form[@class='LoginForm']/fieldset/input").is_enabled()
#
# element = driver.find_element_by_xpath("//form[@class='LoginForm']/button")
# driver.execute_script("arguments[0].click();", element)

