from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\\Users\\lst\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://ep.knou.ac.kr/login.do?epTicket=LOG')

# lists = ['aaaa', 'bbbb', 'cccc']

# for list in lists:
#     print(list)
lists_id = ['a5074','b5074','c5074','d5074','f5074']
lists_pw = ['eogkrrPwjd','eogkrrPwjd1!', 'eogkr']

try:
    for list_id in lists_id:
        for list_pw in lists_pw:
            driver.find_element_by_name('username').send_keys(list_id)
            driver.find_element_by_name('password').send_keys(list_pw)
            driver.find_element_by_id('btn_login').click()
            time.sleep(4)
            driver.find_element_by_xpath('//button/span').click()
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

