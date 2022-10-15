#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File : hesuan_helper.py
@Time : 2022/10/15 19:15:42
@Auth : Ming(<3057761608@qq.com>)
@Vers : 1.0
@Desc : hesuan helper
@Usag : Usag
"""
# here put the import lib
import sys
import time
import pyautogui
import pyperclip

def send_msg(name):
    """
    send msg to name
    """
    # open WeChat
    pyautogui.hotkey('ctrl','alt','w')
    # find name
    pyautogui.hotkey('ctrl','f')
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    # send msg
    msg = '叮叮叮 '+name+'同学。核酸小助手提醒你今天要做核酸啦！今天做完核酸之后记得在高导发的台账里面更新核酸日期~https://docs.qq.com/sheet/DV3BOZ1R5bG1hUkhS'
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    print(name+'has been reminded')

def print_help():
    print('Desc : remind people to do hesuan')
    print('Usag : python main.py -[h|i]')
    print('  -h : print help')
    print('  -i : input names file, like list_1.dat')

def main():
    if '-h' in sys.argv:
        print_help()
        sys.exit(0)
    if '-i' in sys.argv:
        name_file = sys.argv[sys.argv.index('-i')+1]
    else:
        print('please input the names file')
        print_help()
        sys.exit(1)

    for name in open(name_file,encoding='utf-8').readlines():
        name = name.replace('\n','')
        send_msg(name)

if __name__ == '__main__':
    main()
