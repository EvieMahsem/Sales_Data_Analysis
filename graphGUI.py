import tkinter as tk
import querriesGui
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def getData(idList, dtList):
    global identifierList, dataList
    identifierList = idList
    dataList = dtList
    
    startWindow()

def popItemsCountry():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Country Here",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(querriesGui.topSellingProductCountry(popEntry.get()), f"{popEntry.get()}'s Top Selling Products")
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def popItemsCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter City Here",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(querriesGui.topSellingProductCity(popEntry.get()), f"{popEntry.get()}'s Top Selling Products")
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def totalSalesCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Specific City",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(querriesGui.totalSalesPerCity(), "Total Sales Per City", popEntry.get())
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def totalSalesCountry():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    showBarGraph(querriesGui.totalSalesPerCountry(), "Total Sales Per Country")

def totalTopSelling():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    showBarGraph(querriesGui.totalTopSelling(), "Total Sales Per Category")

def topSellingCountry():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Specific Country",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(querriesGui.topSellingCategoryCountry(popEntry.get()), f"{popEntry.get()}'s Total Category Sales")
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def topSellingCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Specific City",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showBarGraph(querriesGui.topSellingCategoryCity(popEntry.get()), f"{popEntry.get()}'s Total Category Sales")
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def productPopYear():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Product Name",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showScatterGraph(querriesGui.productPopYear(popEntry.get()), f"{popEntry.get()}'s Popularity Over the Year", True)
                    )
    popLabel.pack()
    popEntry.pack()
    popButton.pack()

def productPopYearCountry():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter Country Name",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)

    popLabel1 = tk.Label(master=displayFrame,
                        text="Enter Product Name",
                        foreground="white",
                        background="blue")
    popEntry1 = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showScatterGraph(querriesGui.productPopYearCountry(popEntry1.get(), popEntry.get()), f"{popEntry1.get()}'s Popularity Over the Year in {popEntry.get()}", True)
                    
                    )
    popLabel.pack()
    popEntry.pack()
    popLabel1.pack()
    popEntry1.pack()
    popButton.pack()

def productPopYearCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    popLabel = tk.Label(master=displayFrame,
                        text="Enter City Name",
                        foreground="white",
                        background="blue")
    popEntry = tk.Entry(master=displayFrame)

    popLabel1 = tk.Label(master=displayFrame,
                        text="Enter Product Name",
                        foreground="white",
                        background="blue")
    popEntry1 = tk.Entry(master=displayFrame)
    popButton = tk.Button(
                    master=displayFrame,
                    text="Done",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: showScatterGraph(querriesGui.productPopYearCity(popEntry1.get(), popEntry.get()), f"{popEntry1.get()}'s Popularity Over the Year in {popEntry.get()}", True)
                    
                    )
    popLabel.pack()
    popEntry.pack()
    popLabel1.pack()
    popEntry1.pack()
    popButton.pack()


def showScatterGraph(queryInput, title, addDate=False): 

    for widget in displayFrame.winfo_children():
        widget.destroy()

    fig = Figure(figsize = (7, 7), dpi = 100)

    x, y = queryInput

    if addDate:
        for i in range(len(x)):
            x[i] = str(x[i]) + '/2021'

  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(x, y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    fig.suptitle(title, fontsize=20)
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

def showBarGraph(queryInput, title, specific = ""):
    for widget in displayFrame.winfo_children():
        widget.destroy()

    f = Figure(figsize=(7, 7), dpi=100)
    ax = f.add_subplot(111)

    x, y = queryInput
    newx = []
    newy = []
    if len(x) >= 10:
        if specific == "" or specific in x[-10:]:
            newx = x[-10:]
            newy = y[-10:]
        else:

            newx.append(x[x.index(specific)])
            newy.append(y[x.index(specific)])
            for i in x[-9:]:
                newx.append(i)
            for i in y[-9:]:
                newy.append(i)
    else:
        newx = x 
        newy = y

    width = .5

    rects1 = ax.bar(newx, newy, width)
    f.suptitle(title, fontsize=20)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    canvas = FigureCanvasTkAgg(f, master=displayFrame)
    canvas.draw()

    canvas.get_tk_widget().pack()

def startWindow():
    win = tk.Tk()
    win.minsize(700, 700)
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
                    text="Show Total Sales by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: totalSalesCity()
                    )
    plotButton1.pack()

    plotButton4 = tk.Button(
                    master=buttonFrame,
                    text="Show Total Sales by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: totalSalesCountry()
                    )
    plotButton4.pack()

    plotButton2 = tk.Button(
                    master=buttonFrame,
                    text="Show Popular Items by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: popItemsCity()
                    )
    plotButton2.pack()

    plotButton3 = tk.Button(
                    master=buttonFrame,
                    text="Show Popular Items by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: popItemsCountry()
                    )
    plotButton3.pack()

    plotButton5 = tk.Button(
                    master=buttonFrame,
                    text="Show Total Top Selling Categories",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: totalTopSelling()
                    )
    plotButton5.pack()

    plotButton6 = tk.Button(
                    master=buttonFrame,
                    text="Top Selling Categories by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: topSellingCountry()
                    )
    plotButton6.pack()

    plotButton7 = tk.Button(
                    master=buttonFrame,
                    text="Top Selling Categories by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: topSellingCity()
                    )
    plotButton7.pack()

    plotButton8 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity over Year",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: topSellingCity()
                    )
    plotButton8.pack()

    plotButton9 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity over Year",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: productPopYear()
                    )
    plotButton9.pack()

    plotButton10 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity in Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: productPopYearCountry()
                    )
    plotButton10.pack()

    plotButton11 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity in City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="blue",
                    fg="yellow",
                    command= lambda: productPopYearCity()
                    )
    plotButton11.pack()

    win.mainloop()
