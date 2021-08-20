import os, time, sys
import subprocess


def loadScreen():
    print("?/::" , end="")
    for i in range(10):
        sys.stdout.write('\rLoading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rLoading -')
        time.sleep(0.1)
        sys.stdout.write('\rLoading \\')
        time.sleep(1.1)
    sys.stdout.write('\rDone!     ')

os.system('cmd /c"pip install kivy pywin32 pyautogui kivyontop tk psutil"')


print("Installing to desktop, while changing position manually please change path in Windows Scheduler.")


""" getting user name in cmd"""

subprocess = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE)
string1=subprocess.stdout.read()
string_list1=string1.decode().split("\\")
string_list2=string_list1[1].splitlines()

loadScreen()


"""username stored in string_list2[0]"""
cmd_cmdstring="cd c:\\users\\"+str(string_list2[0])+"\\Downloads && move pyeye.py C:\\Users\\"+str(string_list2[0])+"\\Desktop"

os.system('cmd /c "%s" ' %(cmd_cmdstring))

"""20eye.py moved to desktop"""


"""creating schedule"""
path1="C:\\Users\\"+str(string_list2[0]+"\\Desktop\\pyeye.py")
os.system('cmd /k"schtasks /create /sc minute /mo 20 /tn PyEyeCare /tr %s" ' %(path1))


