import tkinter as tk
import pyautogui

clicking = False
miliseconds = 10

root = tk.Tk()
root.title('Auto Clicker')

label = tk.Label(root, text='Click the button!')
label.pack()

def toggle_clicking():
    global clicking, miliseconds
    clicking = not clicking
    if clicking:
        button.config(text='Stop')
        def click():
            if clicking:
                pyautogui.click()
                root.after(miliseconds, click)
        click()
    else:
        button.config(text='Start')
        pyautogui.FAILSAFE = True

button = tk.Button(root, text='Start', command=toggle_clicking)
button.pack()

root.bind('<Control-Shift-b>', toggle_clicking)

root.mainloop()