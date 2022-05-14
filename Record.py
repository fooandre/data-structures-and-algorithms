# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

class Record:
    def __init__(self, *args, customer, package, pax, cost_per_pax):
        self.__customer = customer
        self.__package = package
        self.__pax = pax
        self.__cost_per_pax = cost_per_pax

    def __str__(self, record): return f"{record['customer']} bought {record['package']} for ${record['cost_per_pax']}/pax for {record['pax']}"
