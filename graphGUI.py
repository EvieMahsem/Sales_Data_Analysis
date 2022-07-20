import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

from matplotlib.ft2font import BOLD
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
    
    titleLabel = tk.Label(master=displayFrame,
                        text="Popular Items by Country",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    popLabel = tk.Label(master=displayFrame,
                        text="Select Country",
                        foreground="white",
                        background="#000026"
                        )
    countryOutput = StringVar(displayFrame)
    countryOutput.set(countriesList[0]) # default value

    countryEntry = ttk.Combobox(displayFrame, textvariable=countryOutput)
    countryEntry['values'] = countriesList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: showBarGraph(querriesGui.topSellingProductCountry(countryOutput.get()), f"{countryOutput.get()}'s Top Selling Products")
                    )
    popLabel.place(relx=.5, rely=.33, anchor='center')
    countryEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def popItemsCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    titleLabel = tk.Label(master=displayFrame,
                        text="Popular Items by City",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    popLabel = tk.Label(master=displayFrame,
                        text="Select City",
                        foreground="white",
                        background="#000026")

    cityOutput = StringVar(displayFrame)
    cityOutput.set(citiesList[0]) # default value

    cityEntry = ttk.Combobox(displayFrame, textvariable=cityOutput)
    cityEntry['values'] = citiesList
    
    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: showBarGraph(querriesGui.topSellingProductCity(cityOutput.get()), f"{cityOutput.get()}'s Top Selling Products")
                    )
    popLabel.place(relx=.5, rely=.33, anchor='center')
    cityEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def totalSalesCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()
    
    titleLabel = tk.Label(master=displayFrame,
                        text="Total Sales by City",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')
    
    extrax, extray = 0.1, .43

    popLabel = tk.Label(master=displayFrame,
                        text="Select City",
                        foreground="white",
                        background="#000026")
    
    citiesLabel = tk.Label(master=displayFrame,
                            text="Cities to Show:",
                            foreground="white",
                            background="#000026")

    cityOutput = StringVar(displayFrame)
    cityOutput.set("") # default value

    cityEntry = ttk.Combobox(displayFrame, textvariable=cityOutput)
    cityEntry['values'] = citiesList
    comparing = []


    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [showBarGraph(querriesGui.totalSalesPerCity(), "Total Sales Per City", cityOutput.get()) if len(comparing) == 0 else compareBarGraphs(querriesGui.compareTotalSalesPerCity(comparing), "Total Sales Per City", cityOutput.get())]
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add City",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(cityOutput.get()), tk.Label(master=displayFrame, text=cityOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), cityOutput.set("")]
                    )
                    
    print(comparing)

    popLabel.place(relx=.5, rely=.33, anchor='center')
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    cityEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')
    addButton.place(relx=.5, rely=.44, anchor='center')

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
    
    titleLabel = tk.Label(master=displayFrame,
                        text="Top Selling Categories by Country",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    popLabel = tk.Label(master=displayFrame,
                        text="Select Country",
                        foreground="white",
                        background="#000026")

    countryOutput = StringVar(displayFrame)
    countryOutput.set(countriesList[0]) # default value

    countryEntry = ttk.Combobox(displayFrame, textvariable=countryOutput)
    countryEntry['values'] = countriesList


    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: showBarGraph(querriesGui.topSellingCategoryCountry(countryOutput.get()), f"{countryOutput.get()}'s Total Category Sales")
                    )
    popLabel.place(relx=.5, rely=.33, anchor='center')
    countryEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def topSellingCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    titleLabel = tk.Label(master=displayFrame,
                        text="Top Selling Categories by City",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    popLabel = tk.Label(master=displayFrame,
                        text="Select City",
                        foreground="white",
                        background="#000026")
    cityOutput = StringVar(displayFrame)
    cityOutput.set(citiesList[0]) # default value

    cityEntry = ttk.Combobox(displayFrame, textvariable=cityOutput)
    cityEntry['values'] = citiesList
    
    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: showBarGraph(querriesGui.topSellingCategoryCity(cityOutput.get()), f"{cityOutput.get()}'s Total Category Sales")
                    )
    popLabel.place(relx=.5, rely=.33, anchor='center')
    cityEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def productPopYear():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    comparing = []
    extrax, extray = 0.1, .43

    titleLabel = tk.Label(master=displayFrame,
                        text="Product Popularity Over the Year",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    popLabel = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")

    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productPopYear(comparing), "Product Popularity Over the Year", True)
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.5, rely=.44, anchor='center')
    popLabel.place(relx=.5, rely=.33, anchor='center')
    productEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def productPopYearCountry():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    titleLabel = tk.Label(master=displayFrame,
                        text="Product Popularity in Country",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    comparing = []
    extrax, extray = 0.1, .43

    popLabel = tk.Label(master=displayFrame,
                        text="Select Country",
                        foreground="white",
                        background="#000026")

    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")

    countryOutput = StringVar(displayFrame)
    countryOutput.set(countriesList[0]) # default value

    countryEntry = ttk.Combobox(displayFrame, textvariable=countryOutput)
    countryEntry['values'] = countriesList

    popLabel1 = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList
    
    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productPopYearCountry(comparing, countryOutput.get()), f"Product Popularity in {countryOutput.get()} Over 2021", True)
                    
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.7, rely=.44, anchor='center')
    popLabel.place(relx=.3, rely=.33, anchor='center')
    countryEntry.place(relx=.3, rely=.38, anchor='center')
    popLabel1.place(relx=.7, rely=.33, anchor='center')
    productEntry.place(relx=.7, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def productPopYearCity():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    titleLabel = tk.Label(master=displayFrame,
                        text="Product Popularity in City",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    comparing = []
    extrax, extray = 0.1, .43

    popLabel = tk.Label(master=displayFrame,
                        text="Select City",
                        foreground="white",
                        background="#000026")
    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")
    # popEntry = tk.Entry(master=displayFrame)

    cityOutput = StringVar(displayFrame)
    cityOutput.set(citiesList[0]) # default value

    cityEntry = ttk.Combobox(displayFrame, textvariable=cityOutput)
    cityEntry['values'] = citiesList


    popLabel1 = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productPopYearCity(comparing, cityEntry.get()), f"Product Popularity in {cityEntry.get()} Over 2021", True)
                    
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.7, rely=.44, anchor='center')
    popLabel.place(relx=.3, rely=.33, anchor='center')
    cityEntry.place(relx=.3, rely=.38, anchor='center')
    popLabel1.place(relx=.7, rely=.33, anchor='center')
    productEntry.place(relx=.7, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def totalSalesTime():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    showScatterGraph(querriesGui.totalSalesTime(), "Total Sales By Time", addTime=True)

def productSalesTime():
    for widget in displayFrame.winfo_children():
        widget.destroy()
    
    titleLabel = tk.Label(master=displayFrame,
                        text="Product Sales by Time",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    comparing = []
    extrax, extray = 0.1, .43

    popLabel1 = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")
    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productSalesTime(comparing), "Product Sales by Time", addTime=True)
                    
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.5, rely=.44, anchor='center')
    popLabel1.place(relx=.5, rely=.33, anchor='center')
    productEntry.place(relx=.5, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def countryProductSalesTime():
    for widget in displayFrame.winfo_children():
        widget.destroy()
    
    titleLabel = tk.Label(master=displayFrame,
                        text="Country Product Sales by Time",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')
    
    comparing = []
    extrax, extray = 0.1, .43

    popLabel1 = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")
    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList

    popLabel2 = tk.Label(master=displayFrame,
                        text="Select Country",
                        foreground="white",
                        background="#000026")

    countryOutput = StringVar(displayFrame)
    countryOutput.set(countriesList[0]) # default value

    countryEntry = ttk.Combobox(displayFrame, textvariable=countryOutput)
    countryEntry['values'] = countriesList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productSalesTimeCountry(comparing, countryEntry.get()), f"Product Sales by Time in {countryEntry.get()}", addTime=True)
                    
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.7, rely=.44, anchor='center')
    popLabel1.place(relx=.7, rely=.33, anchor='center')
    productEntry.place(relx=.7, rely=.38, anchor='center')
    popLabel2.place(relx=.3, rely=.33, anchor='center')
    countryEntry.place(relx=.3, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def cityProductSalesTime():
    for widget in displayFrame.winfo_children():
        widget.destroy()

    titleLabel = tk.Label(master=displayFrame,
                        text="City Product Sales by Time",
                        foreground="white",
                        background="#000026",
                        font=('TkDefaultFont', 20))
    titleLabel.place(relx=.5, rely=.05, anchor='center')

    comparing = []
    extrax, extray = 0.1, .43

    popLabel1 = tk.Label(master=displayFrame,
                        text="Select Product",
                        foreground="white",
                        background="#000026")
    citiesLabel = tk.Label(master=displayFrame,
                            text="Products to Show:",
                            foreground="white",
                            background="#000026")

    productOutput = StringVar(displayFrame)
    productOutput.set(productsList[0]) # default value

    productEntry = ttk.Combobox(displayFrame, textvariable=productOutput)
    productEntry['values'] = productsList

    popLabel2 = tk.Label(master=displayFrame,
                        text="Select City",
                        foreground="white",
                        background="#000026")

    cityOutput = StringVar(displayFrame)
    cityOutput.set(citiesList[0]) # default value

    cityEntry = ttk.Combobox(displayFrame, textvariable=cityOutput)
    cityEntry['values'] = citiesList

    popButton = tk.Button(
                    master=displayFrame,
                    text="Show Graph",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: testshowScatterGraph(querriesGui.productSalesTimeCity(comparing, cityEntry.get()), f"Product Sales by Time in {cityEntry.get()}", addTime=True)
                    
                    )
    addButton = tk.Button(
                    master=displayFrame,
                    text="Add Product",
                    width=19,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: [comparing.append(productOutput.get()), tk.Label(master=displayFrame, text=productOutput.get(), foreground="white", background="#2E5984").place(relx=extrax, rely=(extray + 0.05 * len(comparing)), anchor="center"), productOutput.set("")]
                    )
    citiesLabel.place(relx=.1, rely=.43, anchor='center')
    addButton.place(relx=.7, rely=.44, anchor='center')
    popLabel1.place(relx=.7, rely=.33, anchor='center')
    productEntry.place(relx=.7, rely=.38, anchor='center')
    popLabel2.place(relx=.3, rely=.33, anchor='center')
    cityEntry.place(relx=.3, rely=.38, anchor='center')
    popButton.place(relx=.84, rely=.95, anchor='center')

def testshowScatterGraph(queryInput, title, addDate=False, addTime=False): 

    for widget in displayFrame.winfo_children():
        widget.destroy()

    fig = Figure(figsize = (7, 7), dpi = 100)
    plot1 = fig.add_subplot(111)

    for i in queryInput.keys():
        if addDate:
            newx = ['01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021', '07/2021', '08/2021', '09/2021', '10/2021', '11/2021', '12/2021']
            newy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            for x in range(len(queryInput[i])):
                for z in range(len(newx)):
                    if queryInput[i][x][0] == newx[z][:2]:
                        newy[z] = queryInput[i][x][1]

        if addTime:
            newx = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
            newy = [0 for i in range(24)]

            for x in range(len(queryInput[i])):
                for z in range(len(newx)):
                    if queryInput[i][x][0] == newx[z][:2]:
                        newy[z] = queryInput[i][x][1]


  
    # adding the subplot
        
  
    # plotting the graph
        plot1.plot(newx, newy, label=i)
    
    if addDate:
        plt.setp(plot1.get_xticklabels(), rotation=30, horizontalalignment='right')
    else:
        plt.setp(plot1.get_xticklabels(), rotation=90, horizontalalignment='right')

  
    # creating the Tkinter canvas
    fig.suptitle(title, fontsize=20)
    fig.legend(loc="lower left")

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


def showScatterGraph(queryInput, title, addDate=False, addTime=False): 

    for widget in displayFrame.winfo_children():
        widget.destroy()

    fig = Figure(figsize = (7, 7), dpi = 100)

    x, y = queryInput

    if addDate:
        for i in range(len(x)):
            x[i] = str(x[i]) + '/2021'

        newx = ['01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021', '07/2021', '08/2021', '09/2021', '10/2021', '11/2021', '12/2021']
        newy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in x:
            newy[newx.index(i)] = y[x.index(i)]
    
    if addTime:
        newx = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        newy = [0 for i in range(24)]

        for i in range(len(x)):
            for q in range(len(newx)):
                if str(x[i]) == newx[q][:2]:
                    newy[q] = y[i]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(newx, newy)
  
    # creating the Tkinter canvas
    fig.suptitle(title, fontsize=20)
    if addTime:
        plt.setp(plot1.get_xticklabels(), rotation=90, horizontalalignment='right')
    else:
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

def compareBarGraphs(queryInput, title, specific=""):
    for widget in displayFrame.winfo_children():
        widget.destroy()

    f = Figure(figsize=(7, 7), dpi=100)
    ax = f.add_subplot(111)

    newx, newy = queryInput
    width = .5

    rects1 = ax.bar(newx, newy, width)
    f.suptitle(title, fontsize=20)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    canvas = FigureCanvasTkAgg(f, master=displayFrame)
    canvas.draw()

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
    global win
    win = tk.Tk()
    win.minsize(700, 700)
    global buttonFrame, displayFrame

    buttonFrame = tk.Frame(
                master=win,
                relief=tk.RAISED,
                borderwidth=3,
                bg ='#000026'
            )
    displayFrame = tk.Frame(
                    master=win,
                    relief=tk.RAISED,
                    borderwidth=3,
                    bg ='#000026'
                            )

    buttonFrame.pack(side='left', fill='both', expand=False)
    displayFrame.pack(fill = 'both', expand=True)

    plotButton1 = tk.Button(
                    master=buttonFrame,
                    text="Total Sales by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: totalSalesCity()
                    )

    plotButton2 = tk.Button(
                    master=buttonFrame,
                    text="Total Sales by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: totalSalesCountry()
                    )

    plotButton3 = tk.Button(
                    master=buttonFrame,
                    text="Popular Items by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: popItemsCity()
                    )

    plotButton4 = tk.Button(
                    master=buttonFrame,
                    text="Popular Items by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: popItemsCountry()
                    )

    plotButton5 = tk.Button(
                    master=buttonFrame,
                    text="Total Top Selling Categories",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: totalTopSelling()
                    )

    plotButton6 = tk.Button(
                    master=buttonFrame,
                    text="Top Selling Categories by Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: topSellingCountry()
                    )

    plotButton7 = tk.Button(
                    master=buttonFrame,
                    text="Top Selling Categories by City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: topSellingCity()
                    )

    plotButton8 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity over Year",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: productPopYear()
                    )

    plotButton9 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity in Country",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: productPopYearCountry()
                    )

    plotButton10 = tk.Button(
                    master=buttonFrame,
                    text="Product Popularity in City",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: productPopYearCity()
                    )

    plotButton11 = tk.Button(
                    master=buttonFrame,
                    text="Total Sales by Time",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: totalSalesTime()
                    )

    plotButton12 = tk.Button(
                    master=buttonFrame,
                    text="Product Sales by Time",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: productSalesTime()
                    )

    plotButton13 = tk.Button(
                    master=buttonFrame,
                    text="Country Product Sales by Time",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: countryProductSalesTime()
                    )

    plotButton14 = tk.Button(
                    master=buttonFrame,
                    text="City Product Sales by Time",
                    width=25,
                    height=2,
                    pady=5,
                    bg="#00beff",
                    fg="#591277",
                    command= lambda: cityProductSalesTime()
                    )
    plotButton5.pack()
    plotButton11.pack()
    plotButton8.pack()
    plotButton12.pack()
    plotButton2.pack()
    plotButton4.pack()
    plotButton9.pack()
    plotButton6.pack()
    plotButton13.pack()
    plotButton1.pack()
    plotButton3.pack()
    plotButton10.pack()
    plotButton7.pack()
    plotButton14.pack()
    win.mainloop()

products = {"Bodywash": ["Axe", "Old Spice", "Dove Bodywash", "CeraVe", "Nivea", "Olay", 4.97, 8.29, 6.99, 11.99, 8.79, 8.99, [4, 12], [4, 12], [4, 12], [4, 12], [4, 12], [4, 12]],
            "Shampoos/Conditioners": ["Garnier", "Suave", "Herbal Essences", "Dove Shampoo", "TRESemme", "Head & Shoulders", 4.99, 4.99, 6.79, 7.99, 6.29, 5.99, [4, 12], [4, 12], [4, 12], [4, 12], [4, 12], [4, 12]],
            "Toothpaste": ["Colgate", "Crest", "Advance White", "Sensodyne", "Biotene", "Parodontax", 1.97, 2.33, 2.67, 5.99, 6.59, 8.69, [6, 20], [6, 25], [4, 15], [4, 30], [4, 12], [2, 15]],
            "Mouthwash": ["Listerine", "Act", "Peridex", "TheraBreath", 3.89, 4.79, 5.45, 6.67, [4, 15], [4, 30], [4, 12], [2, 15]],
            "Cars/Trucks": ["Ford", "Dodge", "Kia", "Hundai", "Volkswagen", "Nissan", 40000.00, 37564.99, 22590.00, 28150.00, 23128.00, 45030.00, [1, 7], [1, 9], [1, 8], [1, 12], [1, 12], [1, 6]],
            "Clothing": ["Levi", "Abercrombie & Fitch", "Nike", "Gucci", "H&M", "Michael Kors", 33.99, 44.99, 52.99, 350.99, 70.89, 120.99, [3, 7], [2, 10], [2, 15], [1, 5], [1, 8], [1, 12]],
            "Perfume/Cologne": ["Hugo Boss", "Versace", "Dolce & Gabbana", "Calvin Klein", "Christian Dior", "Mont Blanc", 42.99, 51.65, 46.99, 55.99, 118.99, 52.11, [2, 9], [2, 15], [3, 14], [2, 12], [1, 11], [4, 12]],
            "Cellular Devices": ["iPhone", "Samsung", "Huawei", "Motorola", "Nokia", 999.99, 799.99, 975.99, 579.99, 129.89, [4, 25], [3, 19], [4, 23], [4, 12], [2, 15]],
            "Computers": ["Apple", "Dell", "HP", "Sony", "Acer", 1599.99, 499.99, 499.99, 1105.00, 529.99, [4, 25], [3, 19], [4, 23], [4, 12], [2, 15]]}

countries = {"Germany": ["Berlin", "Colgne", "Dresden", "Munich", "Frankfurt", "Stuttgart"],
             "Italy": ["Rome", "Naples", "Milan", "Florence", "Bologna", "Venice"],
             "France": ["Paris", "Bordeaux", "Toulouse", "Nice", "Lyon", "Nantes"],
             "Spain": ["Barcelona", "Madrid", "Seville", "Majorca", "Ibiza", "Valencia"],
             "England": ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow", "Liverpool"],
             "USA": ["Hollywood", "Miami", "Las Vegas", "Dallas", "New York City", "Seattle"]}

productsList = []
citiesList = []
countriesList = ["Germany", "Italy", "France", "Spain", "England", "USA"] 
for i in products.values():
    for x in i[:int(len(i) / 3)]:
        productsList.append(x)

for i in countries.values():
    for x in i:
        citiesList.append(x)
citiesList.sort()
productsList.sort()
countriesList.sort()