# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

from DB import DB


class Menu:
    db = DB()

    __functions = [
        {
            "title": "display records",
            "function": lambda self: self.db.display_all()
        },
        {
            "title": "sort records by customer name",
            "function": lambda self: self.db.try_sort(self.db.bubble)
        },
        {
            "title": "sort records by package",
            "function": lambda self: self.db.try_sort(self.db.selection)
        },
        {
            "title": "sort records by cost",
            "function": lambda self: self.db.try_sort(self.db.insertion)
        },
        {
            "title": "search records for customer",
            "function": lambda self: self.db.try_search(self.db.linear)
        },
        {
            "title": "search records for package",
            "function": lambda self: self.db.try_search(self.db.binary)
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

    def call_func(self, option): self.__functions[option - 1]["function"](self)
