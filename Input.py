def insert_stuff():
    while True:
        print("In this portion ...")
        print("\t1. To go here")
        print("\t2. To go there")
        print("\t3. To go back to the main menu.")
        while True:
            try:
                lel= int(input("\nSelection: "))
            except ValueError:
                print(ValueError)
                print("Please make a proper selection.")
            else:
                break
        if lel == 1:
            pass
        elif lel == 2:
            pass
        elif lel == 3:
            break


def Startup ():
    while True:
        print("Hello!")
        print("\t1. ")
        print("\t2. ")
        print("\t3. To close out the program.")
        while True:
            try:
                sel = int(input("\nSelection: "))
            except (ValueError):
                print("ValueError")
                print("Please make a valid input.")
            else:
                break
        if sel == 1:
            insert_stuff()
        elif sel == 2:
            insert_mstuff()
        elif sel == 3:
            disfile = open('newFile.txt', 'w')
            disfile.write(' ')
            disfile.close()
            print("Alright, catch ya later then.")
            break

Startup()