# Task 5 python program to make Contact Book 
mycontactlist = {}

def display_mycontactlist():
    print("Name\t\tcontact number\t\temail\t\taddress\t\t")
    for key in mycontactlist:
        print("{}\t\t{}\t\t{}\t\t{}".format(key, *mycontactlist.get(key)))

def show_menu():
    print("1. Add new contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

# Main function 
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ") 
        
        if choice == '1':
            Name = input("Enter your Name: ")
            phone = input("Enter your mobile number: ")
            email = input("Enter your email address: ")
            address = input("Enter your address: ")
            mycontactlist[Name] = (phone, email, address)
        
        elif choice == '2':
            if not mycontactlist:
                print("Empty contact book")
            else:
                display_mycontactlist()

        elif choice == '3':
            search_Name = input("Enter the contact Name: ")
            if search_Name in mycontactlist:
                print(search_Name, "'s contact details are:", mycontactlist[search_Name])
            else:
                print("Name is not found in this contact book")
                
        elif choice == '4':
            update_mycontactlist = input("Enter the contact Name to be updated: ")
            if update_mycontactlist in mycontactlist:
                phone = input("Enter new mobile number: ")
                email = input("Enter new email address: ")
                address = input("Enter new address: ")
                mycontactlist[update_mycontactlist] = (phone, email, address)
                print("Contact updated successfully")
                display_mycontactlist()
            else:
                print("Name is not found in mycontactlist")
                
        elif choice == '5':
            del_mycontactlist = input("Enter the contact Name to be deleted: ")
            if del_mycontactlist in mycontactlist:
                confirm = input("Do you want to delete this contact yes/No? ")
                if confirm.lower() == 'yes':
                    mycontactlist.pop(del_mycontactlist)
                    print("Contact deleted.")
                display_mycontactlist()
            else:
                print("Name is not found in this contact book")    
        else:
            break       

if __name__ == "__main__":
    main()