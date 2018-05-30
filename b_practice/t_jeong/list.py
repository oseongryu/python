import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import pymssql

# 키움증권 각 시장에 속하는 종목의 종목 코드 리스트를 얻을 수 있다.
# 자료 표현 : 010140-삼성중공업
class Kiwoom(QAxWidget):
    def __init__(self):
        super(Kiwoom, self).__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(";")
        return code_list[:-1]

    def get_code_list_by_makrket_name(self, market1):
        code_nm = self.dynamicCall("GetMasterCodeName(String)", market1)
        return code_nm

    # MS SQL 서버 연결
    def db_connection(self):
        server = '210.217.42.132'
        user = 'sa'
        password = 'eorlf_1234'

        conn = pymssql.connect(server, user, password, "HOTEL")
        cursor = conn.cursor()
        return cursor

    #


if __name__ == "__main__":
            app = QApplication(sys.argv)
            kiwoom = Kiwoom()
            kiwoom.comm_connect()
            code_list = kiwoom.get_code_list_by_market('0')
            print(len(code_list))
            i = 0
            mkNm = ''

            for code in code_list:
                #최초 첫번째 리스트 mkNm 초기화

               if i == 6:
                  code_name = kiwoom.get_code_list_by_makrket_name(mkNm)
                  print(mkNm + '-' + code_name)
                  mkNm = ''
                  i = 0
               else:
                   mkNm = mkNm + code[i]
                   i = i + 1


                #print(code, end = "")

           #     i = 0
           #     code_name = kiwoom.get_code_list_by_makrket_name(code[i])
           #     print(code_name)
           #     i = i + 1
