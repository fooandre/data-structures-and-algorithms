# About the author
# Name: Andre Foo
# Admin Number: 210119U
# Tut Group: IT2153-07

class DB:
    # region Attributes
    __records = [
        {
            "customer": "sam",
            "package": "basic",
            "pax": 2,
            "cost_per_pax": 300
        },
        {
            "customer": "alex",
            "package": "premium",
            "pax": 5,
            "cost_per_pax": 750
        },
        {
            "customer": "xing jie",
            "package": "premium luxury",
            "pax": 1,
            "cost_per_pax": 1200
        }
    ]

    n = len(__records)
    #endregion

    # region Basic Methods
    def get_all(self): return [record for record in self.__records]

    def display_all(self): [print(f"{self.__records.index(record) + 1} | {str(record)}") for record in self.__records]
    # endregion

    # region DB Methods
    def add(self, record): self.__records.append(record)
    
    def remove(self, record): self.__records.remove(record)
    # endregion

    # region Sorting
    def bubble(self):
        for i in range(self.n - 1, 0, -1):
            for j in range(i):
                if self.__records[j]["customer"] > self.__records[j + 1]["customer"]:
                    tmp = self.__records[j]
                    self.__records[j] = self.__records[j + 1]
                    self.__records[j + 1] = tmp
        self.on_sort_finish()
        return True

    def selection(self):
        for i in range(self.n - 1):
            smallNdx = i

            for j in range(i + 1, self.n):
                if self.__records[j]["package"] < self.__records[smallNdx]["package"]:
                    smallNdx = j

            if smallNdx != i:
                tmp = self.__records[i]
                self.__records[i] = self.__records[smallNdx]
                self.__records[smallNdx] = tmp
        self.on_sort_finish()
        return True

    def insertion(self):
        for cpp in range(1, self.n):
            while True:
                value = self.__records[cpp]
                pos = cpp

                if pos <= 0 or value["cost_per_pax"] >= self.__records[pos - 1]["cost_per_pax"]:
                    break

                self.__records[pos] = self.__records[pos-1]
                pos -= 1
                self.__records[pos] = value
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
        try:
            search = input("Enter search key: ").lower()

            res = [record for record in self.__records if record["customer"].lower()
                   == search]

            if len(res) == 0:
                print("Customer not found")
                return False

            print(f"All records for {search[0].upper() + search[1:]} found")
            [print(f"{res.index(record) + 1} | {record['customer']} bought {record['package']} for ${record['cost_per_pax']}/pax for {record['pax']}") for record in res]
            return res
        except Exception as err:
            print(err)
            return False

    def binary(self):
        try:
            search = input("Enter search key: ").lower()

            start = 0
            end = self.n - 1

            while True:
                midpoint = (end + start) // 2
                pointer = self.data[midpoint]["package"]

                if end < start:
                    print(search, "not found in records")
                    break

                if pointer == search:
                    print(search, "found")
                    res = self.data[midpoint]
                    print(
                        f"{self.data.index(res) + 1} | {res['customer']} bought {res['package']} for ${res['cost_per_pax']}/pax for {res['pax']}")
                    return res

                if pointer > search:
                    end = midpoint - 1
                    continue

                start = midpoint + 1
            print(search, "not found")
            return False
        except Exception as err:
            print(err)
            return False

    def try_search(self, func):
        try:
            return func()
        except Exception as err:
            print(err)
            return False
    # endregion
