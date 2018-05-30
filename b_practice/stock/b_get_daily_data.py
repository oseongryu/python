import sys
from PyQt5.QtWidgets import *
import pykiwoom

print(dir(pykiwoom))

print(pykiwoom.get_daily_data("039490","20180311","20180315",None))