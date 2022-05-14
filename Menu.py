# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

from DB import DB

db = DB()

class Menu:
    __functions = [
        {
            "title": "display records",
            "function": lambda: db.display_all()
        },
        {
            "title": "sort records by customer name",
            "function": lambda: db.try_sort(db.bubble)
        },
        {
            "title": "sort records by package",
            "function": lambda: db.try_sort(db.selection)
        },
        {
            "title": "sort records by cost",
            "function": lambda: db.try_sort(db.insertion)
        },
        {
            "title": "search records for customer",
            "function": lambda: db.try_search(db.linear)
        },
        {
            "title": "search records for package",
            "function": lambda: db.try_search(db.binary)
        },
        {
            "title": "list records by cost range",
            "function": None
        }
    ]

    def display(self):
        print("=== Menu ===")
        [print(f"{self.__functions.index(func) + 1}) {func['title']}") for func in self.__functions]
        print()

    def call_func(self, option): self.__functions[option - 1]["function"]()
