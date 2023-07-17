import json

with open("contact-data.json", "r") as jsonFile:
    data = json.load(jsonFile)

def main():
    while(True):
        print("\n********** Press 1 to list all contacts ***********")
        print("\n********** Press 2 to list current contact*********")
        print("\n********** Press 3 to add contact *****************")
        print("\n********** Press 4 to delete contact **************")
        print("\n********** Press 0 to quit ************************\n")

        try: 
            userOut = int(input("Enter the number: \n"))
        except ValueError:
            print("You enter incorrect nubmer!")

        if userOut == 1:        
            getContacts()
        elif userOut == 2:
            getCurrentCon()
        elif userOut == 3:
            addContact()
        elif userOut == 4:
            deleteContact()
        elif userOut == 0:
            break

def getContacts():
    for item in data:
        userName = item["name"]
        userNumber = item["number"]
        print(f"Name: {userName}, Number: {userNumber}\n")

def getCurrentCon():
    userInput = input("\nEnter contact name: ") 

    for item in data:   
        userName = item["name"] 
        userNumber = item["number"] 
        if userInput == userName:  
            print(f"\nName: {userName}, Number: {userNumber}")
                   
def addContact(): 
    userName = input("\nEnter new contact name: ") 

    for item in data:
        if userName == item["name"]:  
            print("\nContact with this contact name already exist!")
            return 

    userNumber = input("\nEter new contact number: ")

    for item in data:
        if userNumber == item["number"]:
            print("\nContact with this number already exist!")
            return
    
    newItem = {
        "name": userName,
        "number": userNumber
    }
    data.append(newItem)

    with open("contact-data.json", "w") as writeJson:
        json.dump(data, writeJson)
    
    print("\nContact added successfully!\n")

def deleteContact(): 
    userName = input("\nEnter name of conact you want to delete: ")

    for item in data:
        if userName == item["name"]:
            data.remove(item)
        else: 
            print("\nContact doesn't exist!")
            return
    
    with open("contact-data.json", "w") as writeJson:
        json.dump(data, writeJson)


userOut = None
    
main()
