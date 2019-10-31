#orig code: https://www.saltycrane.com/blog/2010/10/how-get-date-n-days-ago-python/
from datetime import datetime, timedelta
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 150)
canvas1.pack()

entry1 = tk.Entry (root)
canvas1.create_window(150, 50, window=entry1)

def getDaDate():

    N =  entry1.get()

    date_N_days_ago = datetime.now() - timedelta(days=int(N))

    label1 = tk.Label(root, text=date_N_days_ago)
    canvas1.create_window(150, 110, window=label1)

button1 = tk.Button(text='Paste days here', command=getDaDate)

canvas1.create_window(150, 80, window=button1)


root.mainloop()