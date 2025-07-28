# def display_menu():
#     print("shopping_list")
#     print("1. add item")
#     print("2. remove item")
#     print("3. view list")
#     print("exit")
# def main():
#     shopping_list = []
#     while True:
#         display_menu()
        # choice = input("enter your choice: ")

        # if choice == 1:
        #     item = input("enter the item to add: ")
        #     if item in shopping_list:
        #         shopping_list.append(item)
        #         print(f"{item} have been added to your shopping list")
        #     else:
        #         print("item not in the shopping list")
        # elif choice == 2:
        #     item = input("enter the item to be removed: ")
        #     if item in shopping_list:
        #         shopping_list.remove(item)
#                 print("f{item} has been removed from the list")
#             else:
#                 print("item not in the shopping list")
#         elif choice == 3:
#             if shopping_list:
#                 print("\nyour shopping list: ")
#                 for i, item in enumerate(shopping_list,start=1):
#                     print(f"{i}. {item}")
#             else:
#                 print("your shopping list is empty")
#         elif choice == 4:
#             print("Goodbye!")
#             break
#         else:
#             print("invalid choice.please try again")
# if __name__=="__main__":
#     main()
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f'"{item}" has been added to your shopping list.')
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from your shopping list.')
            else:
                print(f'"{item}" is not in the shopping list.')

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()