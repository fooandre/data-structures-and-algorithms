# Author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

from DB import DB

db = DB()

class Menu:
    __functions = [
        {
            "title": "Display records",
            "function": lambda: db.display_all()
        },
        {
            "title": "Sort records by customer name",
            "function": lambda: db.try_sort(db.bubble)
        },
        {
            "title": "Sort records by package",
            "function": lambda: db.try_sort(db.selection)
        },
        {
            "title": "Sort records by cost",
            "function": lambda: db.try_sort(db.insertion)
        },
        {
            "title": "Sort records by no of pax",
            "function": lambda: db.try_sort(db.counting)
        },
        {
            "title": "Search records for customer",
            "function": lambda: db.try_search(db.linear)
        },
        {
            "title": "Search records for package",
            "function": lambda: db.try_search(db.binary)
        },
        {
            "title": "List records by cost range",
            "function": lambda: db.find_in_range()
        }
    ]

    def display(self):
        print("=== Menu ===")
        [print(f"{self.__functions.index(func) + 1}) {func['title']}") for func in self.__functions]
        print()

    def call_func(self, option): self.__functions[option - 1]["function"]()
