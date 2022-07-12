from csv import writer
import names
import random
import time

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    newTime = time.strftime(time_format, time.localtime(ptime))[11:16]
    amOrPM = time.strftime(time_format, time.localtime(ptime))[-2:]

    if amOrPM == 'PM' and newTime[:2] != '12' and newTime[:2] != '11' and newTime[:2] != '10':
        newNum = int(newTime[1]) + 12
        newTime = str(newNum) + newTime[-3:]
    elif amOrPM == 'PM' and newTime[:2] != '12':
        newNum = int(newTime[:2]) + 12
        newTime = str(newNum) + newTime[-3:]
    elif amOrPM == 'AM' and newTime[:2] == '12':
        newTime = '00' + newTime[-3:]

    datetime = time.strftime(time_format, time.localtime(ptime))[:11] + newTime

    return datetime


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def appendRow(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def getinputs(num):
    for i in range(1, num + 1):
        inputList = []
        productCategories = [i for i in products.keys()]
        countriesList = [i for i in countries.keys()]

        customerName = random.choice(fullNames)
        productCategory = random.choice(productCategories)
        productName = random.choice(products[productCategory][:int(len(products[productCategory]) / 3)])
        paymentType = random.choice(paymentTypes)
        country = random.choice(countriesList)
        city = random.choice(countries[country])
        websiteName = random.choice(websites)
        transactionSuccess = 'Y'
        quantityRange = products[productCategory][products[productCategory].index(productName) + (2 * int(len(products[productCategory]) / 3))]
        quantity = random.randint(quantityRange[0], quantityRange[1])
        
        if random.uniform(0, 1) < 0.05:
            quantity = random.randint(20000, 100000)

        price = products[productCategory][products[productCategory].index(productName) + (int(len(products[productCategory]) / 3))] * quantity


        if random.uniform(0, 1) < 0.05:
            transactionSuccess = 'N'
        #orderID, customerID, customerName, productID, productName, productCategory, paymentType, quantity, price, datetime, country, city, website, transactionID, transactionSuccess, failureReason

        inputList.append(i)
        inputList.append(fullNames.index(customerName) + 100)
        inputList.append(customerName)
        inputList.append(1000 + (100 * productCategories.index(productCategory)) + (products[productCategory].index(productName)))
        inputList.append(productName)
        inputList.append(productCategory)
        inputList.append(paymentType)
        inputList.append(quantity)
        inputList.append("{:0.2f}".format(price))
        inputList.append(random_date("1/1/2021 12:00 AM", "12/31/2021 11:59 PM", random.random()))
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
                inputList.append("Could not complete transfer")
            elif paymentType == "Wallet":
                inputList.append("Invalid CVV")
        else:
            inputList.append(" ")
             
        appendRow('csvGenerator/data.csv', inputList)

paymentTypes = ["Card", "Internet Banking", "UPI", "Wallet"]
fullNames = [names.get_full_name() for i in range(100)]
websites = ["www.amazon.com", "www.ebay.com", "www.alibaba.com", "www.taobao.com", "www.walmart.com", "www.etsy.com", "www.craigslist.com", "www.target.com"]

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

getinputs(10000)

