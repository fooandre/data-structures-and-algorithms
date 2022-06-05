# Author
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

    def edit(self):
        print(f"\n{self}\n(1) Customer name\n(2) Package Name\n(3) No of pax\n(4) Cost per pax")
        
        while True:
            to_edit = input("Enter attribute to edit or press \"enter\" to cancel: ").strip().lower()
            
            if to_edit == '':
                print("\nRecord saved!")
                break
            elif to_edit == '1':
                new_value = input("Enter new customer name or press \"enter\" to cancel: ")
                if new_value == '': break
                self.__customer = new_value[0].upper() + new_value[1:]
            elif to_edit == '2':
                new_value = input("Enter new package name or press \"enter\" to cancel: ")
                if new_value == '': break

                self.__package = new_value[0].upper() + new_value[1:]
            elif to_edit == '3':
                while True:
                    new_value = input("Enter new no of pax or press \"enter\" to cancel: ")
                    if new_value == '': break

                    if not new_value.isnumeric():
                        print("Value must be integer, please try again or press \"enter\" to cancel!\n")
                        continue
                    
                    self.__pax = int(new_value)
                    break
            elif to_edit == '4':
                while True:
                    new_value = input("Enter new cost per pax or press \"enter\" to cancel: ")
                    if new_value == '': break

                    try:
                        new_value = float(new_value)
                        self.__cost_per_pax = new_value
                        break
                    except:
                        print("Value must be numeric, please try again or press \"enter\" to cancel!\n")
                        continue
            else:
                print("That was not one of the options, please try again or press \"enter\" to cancel")
