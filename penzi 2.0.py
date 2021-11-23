#coding=utf-8
import win32api
import pyperclip
import win32con
import time
import random

print("-----------------------------------------------------------------------")
print("使用方法：设置好参数，在10秒内打开聊天窗口")
print()
print("                                        --------code by bemo")
print("-----------------------------------------------------------------------")


words = input("要骂的话:")
numb = input("骂人次数:")
pyperclip.copy(words)

#倒计时
print()
print("我数到10秒：")
for i in range(11):
    print("\r"+str(i)+"s",end="")
    time.sleep(1)


def kaima():
        win32api.keybd_event(17,0,0,0)  #ctrl
        win32api.keybd_event(86,0,0,0)  #v
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) 
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)#enter
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.2)

i = 0
while int(i) <= int(numb):
    kaima()
    i =  i + 1

print()
input("已骂")
