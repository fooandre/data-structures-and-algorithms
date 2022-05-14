# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

from DB import DB
from Menu import Menu

if __name__ == "__main__":
    menu = Menu()
    db = DB()

    db.add(customer="alex", package="premium", pax=2, cost_per_pax=750)
    db.add(customer="sam", package="basic", pax=5, cost_per_pax=300)
    db.add(customer="alex", package="premium luxury", pax=1, cost_per_pax=1200)

    # db.try_sort(db.insertion)

    print()
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
