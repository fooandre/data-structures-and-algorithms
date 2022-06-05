# Author
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
    db.add(customer="perry", package="premium", pax=3, cost_per_pax=1700)
    db.add(customer="tristan", package="basic", pax=10, cost_per_pax=2000)
    db.add(customer="jordan", package="basic", pax=1, cost_per_pax=3200)
    db.add(customer="michael", package="premium", pax=8, cost_per_pax=3200)
    db.add(customer="denise", package="premium luxury", pax=1, cost_per_pax=200)
    db.add(customer="daryl", package="basic", pax=1, cost_per_pax=100)
    db.add(customer="sam", package="premium luxury", pax=1, cost_per_pax=100)

    print()
    while True:
        menu.display()

        res = input("Select an option: ").strip().lower()

        if (res == ''):
            print("Exiting program...")
            break

        try:
            res = int(res)
            menu.call_func(res)
        except Exception as e: print("That is not an option on the menu, try again")
        finally: print()
