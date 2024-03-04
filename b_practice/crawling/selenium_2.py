from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)

# 웹 사이트 열기
browser.get('https://www.naver.com')

# 쇼핑 메뉴 클릭하기
browser.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()
time.sleep(2)

# 새창을 바라보게 만들기
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# 화면 최대화 해야지 검색창이 보임
browser.maximize_window()

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys("아이폰13")
search.send_keys(Keys.ENTER)