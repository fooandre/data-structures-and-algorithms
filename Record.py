# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

class Record:
    def __init__(self, *args, customer, package, pax, cost_per_pax):
        self.__customer = customer[0].upper() + customer[1:].lower()
        self.__package = package[0].upper() + package[1:].lower()
        self.__pax = pax
        self.__cost_per_pax = cost_per_pax

    def __str__(self): return f"{self.__customer} bought {self.__package} for ${self.__cost_per_pax}/pax for {self.__pax}"

    def get_customer(self): return self.__customer.lower()

    def get_package(self): return self.__package.lower()

    def get_pax(self): return self.__pax

    def get_cost_per_pax(self): return self.__cost_per_pax
