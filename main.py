import pyautogui, psutil, time, win32process, threading, datetime, tkinter
from win32gui import GetForegroundWindow
width, height = pyautogui.size()

process_time = {}
formatted_process_time = {}
def calcProcessTime():

    timestamp = {}
    while True:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(
            ".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0
        new_time=process_time[current_app] + int(time.time()) - timestamp[current_app]
        process_time[current_app] = new_time
        formatTime()

def formatTime():
    for key in process_time.keys():
        x = datetime.timedelta(seconds=process_time[key])
        formatted_process_time[key] = str(x)








def refreshTable():
    counter = 1
    for key in formatted_process_time.keys():
        tkinter.Label(root, text=(key[0].upper() + key[1:])).grid(row=counter, column=1)
        tkinter.Label(root, text=(formatted_process_time[key])).grid(row=counter, column=2)

        counter += 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calcThread = threading.Thread(target=calcProcessTime, args=(), daemon=True)
    calcThread.start()
    time.sleep(3)
    # kivyApp = UsageApp()
    # kivyApp.run()
    root = tkinter.Tk()
    global counter
    refreshTable()
    tkinter.Button(root, text="Refresh", command=refreshTable).grid(row=root.grid_size()[1]-2 , column=1)
    root.mainloop()


