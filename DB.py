# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

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

        for i in range(n - 1, 0, -1):
            for j in range(i):
                if data[j].get_customer() > data[j + 1].get_customer():
                    tmp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = tmp

        self.on_sort_finish()
        return True

    def selection(self):
        data = self.get_all()
        n = len(data)

        for i in range(n - 1):
            smallNdx = i

            for j in range(i + 1, n):
                if data[j].get_package() < data[smallNdx].get_package(): smallNdx = j

            tmp = data[i]
            data[i] = data[smallNdx]
            data[smallNdx] = tmp
            
        self.on_sort_finish()
        return True

    def insertion(self):
        data = self.get_all()
        n = len(data)

        for i in range(1, n):
            while True:
                value = data[i]
                pos = i

                if pos <= 0 or value.get_cost_per_pax() >= data[pos - 1].get_cost_per_pax():
                    break

                data[pos] = data[pos-1]
                pos -= 1
                data[pos] = value
        self.on_sort_finish()
        return True

    def try_sort(self, func):
        try:
            return func()
        except Exception as err:
            print(err)
            return False

    def on_sort_finish(self):
        print("Records sorted\n")
        self.display_all()
    # endregion

    # region Searching
    def linear(self):
        search = input("Enter search key: ").lower()

        res = [record for record in self.get_all() if record.get_customer()
                == search]

        if len(res) == 0:
            print("Customer not found")
            return False

        [print(f"{res.index(record) + 1} | {record}") for record in res]
        return res

    def binary(self):
        search = input("Enter search key: ").lower()

        data = self.get_all()
        start = 0
        end = len(data) - 1

        while True:
            midpoint = (end + start) // 2
            pointer = data[midpoint].get_package()

            if end < start:
                break

            if pointer == search:
                res = data[midpoint]
                print(f"{data.index(res) + 1} | {res}")
                return res

            if pointer > search:
                end = midpoint - 1
                continue

            start = midpoint + 1

        print(search, "not found")

    def try_search(self, func):
        try:
            return func()
        except Exception as err:
            print(err)
            return False
    # endregion
