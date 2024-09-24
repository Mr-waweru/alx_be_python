def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Item to add: ")
            shopping_list.append(item)
            print()
            print(f"'{item}' has/have been added to shoppinglist")
            
        elif choice == '2':
            item = input("Item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has/ have been removed from shoppinglist")
            else:
                print(f"{item} not found")
            
        elif choice == '3':
            print("Current Shooping List")
            

            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    print(shopping_list)


if __name__ == "__main__":
    main()










