# -*-coding: cp949 -*-
import pyautogui
import sys
import time

print('####################################################')
print('######################### by zeromini  `18.3.5 #####')
print('######################################### ver 0.02 #')
print('####################################################')
print('####################################################')

def keyboard_macro():
    time.sleep(5)
    pyautogui.keyDown('alt')
    time.sleep(5)
    pyautogui.press('t')
    time.sleep(5)
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.press('r')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.keyDown('alt')
    time.sleep(5)
    pyautogui.press('t')
    time.sleep(5)
    pyautogui.keyUp('alt')
    time.sleep(5)
    pyautogui.press('s')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)


sign = str(input('>>'))

if sign == 'A':
    print(' Automouse is running')
    while True:
        if sign == 'Y':
            print(' ���콺 ��ǥ�� �б����� ���ϴ� ��ġ�� ���콺�� ���� Y�� �����ּ��� ')
            sign2 = str(input('>>'))
            if sign2 == 'Y':
                x, y = pyautogui.position()
                print(' �Է��Ͻ� ��ǥ����  {}, {}'.format(x,y))
                sys.stdout.flush()
            print(' Delay Time�� �Է����ּ��� Ex) 5 = 5��, 300 = 5��')
            time2 = int(input('>>'))
            print(time2)
            print(' ���α׷��� ���� �˴ϴ�..........')
            print(' ���α׷��� �����ϱ� ���ؼ��� ������ X �ڽ��� �����ּ���')
            while True:
                pyautogui.click(x,y)
                time.sleep(time2)

                pyautogui.press('enter')


elif sign == 'K':
    print('  Delay Time�� �Է����ּ��� Ex) 5 = 5��, 300 = 5��')
    time2 = int(input('>>'))
    print(time2)
    print(' ���α׷� ������ ���� �մϴ� ')
    print(' ���α׷��� �����ϱ� ���ؼ��� ������ X �ڽ��� �����ּ���')
    while True:

         keyboard_macro()
         time.sleep(time2)