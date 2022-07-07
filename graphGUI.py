import tkinter as tk
import random
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def getData(idList, dtList):
    global identifierList, dataList
    identifierList = idList
    dataList = dtList
    
    startWindow()


def showScatterGraph(idList, dataList): 

    for widget in displayFrame.winfo_children():
        widget.destroy()

    fig = Figure(figsize = (7, 7), dpi = 100)

    x = idList
    y = dataList
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(x, y)
    plot1.set_xlabel("Hello")
    plot1.set_ylabel("World")
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    plt.setp(plot1.get_xticklabels(), rotation=30, horizontalalignment='right')

    canvas = FigureCanvasTkAgg(fig,
                               master = displayFrame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window=displayFrame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def showBarGraph(idList, dataList):
    for widget in displayFrame.winfo_children():
        widget.destroy()

    f = Figure(figsize=(7, 7), dpi=100)
    ax = f.add_subplot(111)

    data = dataList
    # ind = np.arange(1, len(inputList) + 1)  # the x locations for the groups
    ind = idList
    width = .5

    rects1 = ax.bar(ind, data, width)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    canvas = FigureCanvasTkAgg(f, master=displayFrame)
    canvas.draw()

    canvas.get_tk_widget().pack()

def startWindow():
    win = tk.Tk()
    win.minsize(500, 500)
    global buttonFrame, displayFrame

    buttonFrame = tk.Frame(
                master=win,
                relief=tk.RAISED,
                borderwidth=3,
                bg='#2E5984'
            )
    displayFrame = tk.Frame(
                    master=win,
                    relief=tk.RAISED,
                    borderwidth=3,
                    bg='#2E5984'
                            )

    buttonFrame.pack(side='left', fill='both', expand=False)
    displayFrame.pack(fill = 'both', expand=True)


    # greeting = tk.Label(master=buttonFrame,
    #                     text="Hello, Tkinter",
    #                     foreground="white",
    #                     background="blue")
    # greeting.pack()

    plotButton1 = tk.Button(
                    master=buttonFrame,
                    text="Show y = x^2",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showScatterGraph([i**2 for i in range(101)])
                    )
    plotButton1.pack()

    plotButton2 = tk.Button(
                    master=buttonFrame,
                    text="Show Scatter Graph",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showScatterGraph(identifierList, dataList)
                    )
    plotButton2.pack()

    plotButton3 = tk.Button(
                    master=buttonFrame,
                    text="Show Bar Graph",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(identifierList, dataList) 
                    )
    plotButton3.pack()

    win.mainloop()

# queryData = query.sort(f'{groupByVar}').collect()
#                 identifierList = [row[0] for row in queryData]
#                 dataList = [int(row[len(row) - 1]) for row in queryData]
#                 print(identifierList)
#                 print(dataList)
#                 graphGUI.getData(identifierList, dataList)