#coding:euc-kr

from pywinauto import application
from pywinauto import timings
import time
import os


# http://blog.naver.com/PostView.nhn?blogId=sfairan&logNo=220784921385&parentCategoryNo=&categoryNo=10&viewDate=&isShowPopularPosts=false&from=postView

app = application.Application()
app.start("C:\\KiwoomFlash3\\Bin\\NKMiniStarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys('xxxx')

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys('yyyy!')

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(50)
os.system("taskkill /im khmini.exe")
