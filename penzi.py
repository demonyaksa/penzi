#coding=utf-8
import win32api
import win32con
import time

print("把要骂的话复制到粘贴板，打开本程序，在10秒内打开聊天窗口")
print()
print("                                 -------------------------code by bemo")
numb = input("骂人次数:")

time.sleep(8)

def kaima():
        win32api.keybd_event(17,0,0,0)  #ctrl
        win32api.keybd_event(86,0,0,0)  #v
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) 
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)#enter
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.5)

i = 0
while int(i) <= int(numb):
    kaima()
    i =  i + 1