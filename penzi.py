#coding=utf-8
import win32api
import win32clipboard as w
import win32con
import time

print("-----------------------------------------------------------------------")
print("设置好参数，在10秒内打开聊天窗口")
print()
print("                                        --------code by bemo")
print("-----------------------------------------------------------------------")
words = input("要骂的话:")
numb = input("骂人次数:")
time.sleep(8)

def setText(aString):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardText(aString)  
    w.CloseClipboard()


def kaima():
        win32api.keybd_event(17,0,0,0)  #ctrl
        win32api.keybd_event(86,0,0,0)  #v
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) 
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(13,0,0,0)#enter
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.5)

i = 0
setText(words)
while int(i) <= int(numb):
    kaima()
    i =  i + 1
