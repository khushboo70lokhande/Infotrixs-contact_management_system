


import csv
def print_menu():
    print("CONTACT MANGEMENT SYSTEM")
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. search a Phone Number')
    print('4. update the number')
    print('5. delete the number')
    print('6. Quit')
    print()
    menu_choice = 0

numbers = {}
print_menu()
menu_choice = 0
while menu_choice != 6:
    menu_choice = int(input("Type in a number (1-5): "))
    
    if menu_choice == 1:
        print("Telephone Numbers:")
        print("the printing can be done by dict as well as csv file")
        print("enter D for printing numbers from dict\n enter C for printing numbers from Csv files")
        ch=input("enter your choice")
        
        #this prints value from csv files
        if ch == "C" or ch == "c":
            with open('contact.csv' , mode = 'r') as file:
                csvFile = csv.reader(file) 
                for lines in csvFile: 
                    print(lines)   
            
        #this prints value from dict
        elif ch == "D" or ch == "d":
            for x in numbers.keys():
                print("Name: ", x, "\nNumber:", numbers[x])
            print()
            
        else:
            print("Wrong input for printing")
        print_menu()
            
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        if len(phone)==10:
            print("invalid contact number")
        elif name in numbers :
                numbers[name]+= " & "+phone
        else:
                numbers[name] = phone
                
        #lets put input in simple I/O file
        fields=["Name",
                "Phone_no."]
        val=numbers.values()
        ke=numbers.keys()
        with open('contact.csv' , mode = 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)  
            writer.writerow(ke)
            writer.writerow(val)
        print_menu()
        
    elif menu_choice == 3:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
        print_menu()
            
    elif menu_choice == 4:
        print("update the contact")
        name=input("Name: ")
        if name in numbers:
            phone=input("Number: ")
            numbers[name] = phone
        else:
            print('Name not exist just add the contact')
        
        fields=["Name",
                "Phone_no."]
        val=numbers.values()
        ke=numbers.keys()
        with open('contact.csv' , mode = 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)  
            writer.writerow(ke)
            writer.writerow(val)
        print_menu()
        
        
    elif menu_choice == 5:
        print("lets delete the contact ")
        name=input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print("The contact is not in the phonebook")

        fields=["Name",
                "Phone_no."]
        val=numbers.values()
        ke=numbers.keys()
        with open('contact.csv' , mode = 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)  
            writer.writerow(ke)
            writer.writerow(val)
        print_menu()
        
    elif menu_choice != 6:
        print("Wrong input : no operation exist for it")
        print_menu()
