# Author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

import re

from Record import Record


class DB:
    # region Attributes
    __records = []
    #endregion

    # region DB Methods
    def get_all(self): return self.__records
    def display_all(self): [print(f"{self.get_all().index(record) + 1} | {record}") for record in self.get_all()]

    def add(self, *args, customer, package, pax, cost_per_pax): self.get_all().append(Record(customer=customer, package=package, pax=pax, cost_per_pax=cost_per_pax))
    def remove(self, record): self.get_all().remove(record)
    # endregion

    # region Sorting
    def bubble(self):
        data = self.get_all()
        n = len(data)

        for i in range(n-1):
            for j in range(0, n-(i+1)):
                if data[j].get_customer() > data[j+1].get_customer():
                    data[j], data[j+1] = data[j+1], data[j] 


    def selection(self):
        data = self.get_all()
        n = len(data)

        for i, record in enumerate(data):
            min = record
            for j in range(i+1, n):
                if data[j].get_package() < min.get_package():
                    data[j], min = min, data[j]
            data[i], min = min, data[i]


    def insertion(self):
        data = self.get_all()
        n = len(data)

        for i in range(n):
            for j in range(i, n):
                if data[j].get_cost_per_pax() < data[i].get_cost_per_pax():
                    data[j], data[i] = data[i], data[j]


    def counting(self):
        data = self.get_all()
        n = len(data)
        
        counts = {}
        i = total = 0
        while total < len(data):
            counts[i] = len([record for record in data if record.get_pax() == i])
            total += counts[i]
            i += 1

        counts = dict(sorted(counts.items(), key=lambda count:count[0]))
        
        for count in counts:
            if count + 1 == len(counts): break
            counts[count+1] += counts[count]

        for count in range(max(counts), 0, -1): counts[count] = counts[count - 1]

        res = [0] * len(data)
        for record in data:
            slot = counts[record.get_pax()]
            res[slot] = record
            counts[record.get_pax()] += 1

        for record in range(len(res)): self.get_all()[record] = res[record]

    def try_sort(self, func):
        try:
            func()
            self.on_sort_finish()
            return True
        except Exception as err:
            print(err)
            return False

    def on_sort_finish(self):
        print("Records sorted\n")
        self.display_all()
    # endregion

    # region Searching
    def linear(self):
        search = input("Enter customer name to search for: ").strip().lower()
        res = [record for record in self.get_all() if record.get_customer() == search]

        if len(res) == 0: 
            print(search, "not found")
            return -1

        return res

    def binary(self):
        self.selection()
        search = input("Enter package name to search for: ").strip().lower()

        data = self.get_all()
        start = 0
        end = len(data) - 1

        while True:
            midpoint = (end + start) // 2
            pointer = data[midpoint].get_package()

            if end < start:
                break

            if pointer == search:
                lower_bound = upper_bound = midpoint

                while lower_bound > start and data[lower_bound-1].get_package() == search: lower_bound -= 1
                while upper_bound < end and data[upper_bound+1].get_package() == search: upper_bound += 1

                return self.get_all()[lower_bound:upper_bound+1]

            if pointer > search:
                end = midpoint - 1
                continue

            start = midpoint + 1

        print(search, "not found")
        return -1

    def find_in_range(self):
        while True:
            lower_bound = input("Enter lower bound: ").strip().lower()

            if not lower_bound.isdecimal() or not lower_bound.isnumeric():
                print("Lower bound must be a number, try again.\n")
                continue

            break

        while True:
            upper_bound = input("Enter upper bound: ").strip().lower()

            if not upper_bound.isdecimal() or not upper_bound.isnumeric():
                print("Upper bound must be a number, try again.\n")
                continue

            break

        res = [record for record in self.get_all() if record.get_cost_per_pax() >= int(lower_bound) and record.get_cost_per_pax() <= int(upper_bound)]
        [print(f"{res.index(record) + 1} | {record}") for record in res]

    def try_search(self, func):
        try:
            res = func()
            self.on_search_finish(res)
            return True
        except Exception as err:
            print(err)
            return False
    
    def on_search_finish(self, res):
        if res != -1:
            [print(f"{res.index(record) + 1} | {record}") for record in res]

            while True:
                to_edit = input("Which record do you want to edit? (press \"enter\" to skip) ").strip().lower()

                if to_edit == '':
                    print("Printing records...\n")
                    break

                if not to_edit.isnumeric():
                    print("Input must be numeric, please try again.\n")
                    continue

                to_edit = int(to_edit)
                if to_edit <= 0 or to_edit > len(res):
                    print("Number not in range, please try again.\n")
                    continue

                res[to_edit - 1].edit()

        print()
        self.display_all()
    # endregion
