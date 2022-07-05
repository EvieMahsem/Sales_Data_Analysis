from csv import writer
import random

def appendRow(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def createFullNames():
    with open('fullNames.txt', 'a') as f:
        for i in range(100):
            f.write(f"{firstNames[random.randint(0, len(firstNames) - 1)]} {lastNames[random.randint(0, len(lastNames) - 1)]}\n")

paymentTypes = ["Card", "Internet Banking", "UPI", "Wallet"]

with open('firstNames.txt', 'r') as f:
    firstNames = [line.rstrip('\n') for line in f]

with open('lastNames.txt', 'r') as f:
    lastNames = [line.rstrip('\n') for line in f]
    
appendRow('data.csv', ['Hello', 'World'])

