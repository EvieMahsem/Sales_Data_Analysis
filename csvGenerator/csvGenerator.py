from csv import writer
import random

def appendRow(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def createFullNames(num):

    with open('firstNames.txt', 'r') as f:
        firstNames = [line.rstrip('\n') for line in f]

    with open('lastNames.txt', 'r') as f:
        lastNames = [line.rstrip('\n') for line in f]

    with open('fullNames.txt', 'a') as f:
        for i in range(num):
            f.write(f"{firstNames[random.randint(0, len(firstNames) - 1)]} {lastNames[random.randint(0, len(lastNames) - 1)]}\n")

def getinputs(num):
    with open('fullNames.txt', 'r') as f:
        fullNames = [line.rstrip('\n') for line in f]

    with open('ecommerce.txt', 'r') as f:
        websites = [line.rstrip('\n') for line in f]
    
    for i in range(1, num + 1):
        inputList = []
        productCategories = [i for i in products.keys()]
        countriesList = [i for i in countries.keys()]

        customerName = random.choice(fullNames)
        productCategory = random.choice(productCategories)
        productName = random.choice(products[productCategory])
        paymentType = random.choice(paymentTypes)
        country = random.choice(countriesList)
        city = random.choice(countries[country])
        websiteName = random.choice(websites)
        transactionSuccess = 'Y'

        if random.uniform(0, 1) < 0.05:
            transactionSuccess = 'N'
        #orderID, customerID, customerName, productID, productName, productCategory, paymentType, quantity, price, datetime, country, city, website, transactionID, transactionSuccess, failureReason

        inputList.append(i)
        inputList.append(fullNames.index(customerName) + 100)
        inputList.append(customerName)
        print(products[productCategory])
        inputList.append(1000 + (100 * productCategories.index(productCategory)) + (products[productCategory].index(productName)))
        inputList.append(productName)
        inputList.append(productCategory)
        inputList.append(paymentType)
        # inputList.append(quantity)
        # inputList.append(price)
        # inputList.append(datetime)
        inputList.append(country)
        inputList.append(city)
        inputList.append(websiteName)
        inputList.append(i + 10000)
        inputList.append(transactionSuccess)

        if transactionSuccess == 'N':
            if paymentType == "Card":
                inputList.append("Invalid card number")
            elif paymentType == "Internet Banking":
                inputList.append("Could not complete transfer")
            elif paymentType == "UPI":
                inputList.append("WHAT IS A UPI")
            elif paymentType == "Wallet":
                inputList.append("Invalid CVV")
             
        appendRow('data.csv', inputList)

paymentTypes = ["Card", "Internet Banking", "UPI", "Wallet"]

products = {"Bodywash": ["Axe", "Old Spice", "Dove", "CeraVe", "Nivea", "Olay"],
            "Shampoos/Conditioners": ["Garnier", "Suave", "Herbal essences", "Dove", "TRESemme", "Head & Shoulders"],
            "Toothpaste": ["Colgate", "Crest", "Advance White", "Sensodyne", "Biotene", "Parodontax"],
            "Mouthwash": ["Listerine", "Act", "Peridex", "TheraBreath"],
            "Cars/Trucks": ["Ford", "Dodge", "Kia", "Hundai", "Volkswagen", "Nissan"],
            "Clothing": ["Levi", "Abercrombie & Fitch", "Nike", "Gucci", "H&M", "Michael Kors"],
            "Perfume/Cologne": ["Hugo Boss", "Versace", "Dolce & Gabbana", "Calvin Klein", "Christian Dior", "Mont Blanc"],
            "Cellular Devices": ["iPhone", "Samsung", "Huawei", "Motorola", "Nokia"],
            "Computers": ["Apple", "Dell", "HP", "Sony", "Acer"]}

countries = {"Germany": ["Berlin", "Colgne", "Dresden", "Munich", "Frankfurt", "Stuttgart"],
             "Italy": ["Rome", "Naples", "Milan", "Florence", "Bologna", "Venice"],
             "France": ["Paris", "Bordeaux", "Toulouse", "Nice", "Lyon", "Nantes"],
             "Spain": ["Barcelona", "Madrid", "Seville", "Majorca", "Ibiza", "Valencia"],
             "England": ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow", "Liverpool"],
             "USA": ["Hollywood", "Miami", "Las Vegas", "Dallas", "New York City", "Seattle"]}

getinputs(10)

