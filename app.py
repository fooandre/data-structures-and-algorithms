# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

from Menu import Menu

if __name__ == "__main__":
    menu = Menu()
    
    while True:
        menu.display()

        res = input("Select an option: ").lower()

        if (res == 'q'):
            print("Exiting program...")
            break

        try:
            res = int(res)
            menu.call_func(res)
        except Exception as e:
            print(e)
            # print("That is not an option on the menu, try again")
        finally:
            print()
