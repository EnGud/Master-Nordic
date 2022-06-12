
class RAM(Size, TestEntity):
    def __init__(self, Size):
        self.Size = Size
        self.data = [None] * Size
        self.TestEntity = TestEntity
        self.TestEntity.TestEntity_count = 0
        self.TestEntity.RAM_put = 0
        self.RAM_get = 0
        self.TestEntity.TestEntity_count_check = 0
        self.TestEntity.TestEntity_count_free = 0
        self.TestEntity.TestEntity_count_error = 0

    def put(self, data):
        self.TestEntity.RAM_put += 1
        if self.TestEntity.RAM_put == 1:
            print("put function called once")
        elif self.TestEntity.RAM_put > 1:
            print("put function called", self.TestEntity.RAM_put, "times")
        if self.TestEntity.TestEntity_count_error == 0:
            for i in range(len(self.data)):
                if self.data[i] == None:
                    self.data[i] = data
                    return i
            print("No space left in the RAM")
            self.TestEntity.TestEntity_count_error += 1
            return -1

    def get(self, adress):
        self.RAM_get += 1
        if self.RAM_get == 1:
            print("get function called once")
        elif self.RAM_get > 1:
            print("get function called", self.RAM_get, "times")
        if self.TestEntity.TestEntity_count_error == 0:
            if self.data[adress] == None:
                print("Data not in the RAM")
                self.TestEntity.TestEntity_count_error += 1
                return -1
            else:
                return self.data[adress]

    def check(self):
        self.TestEntity.TestEntity_count_check += 1
        if self.TestEntity.TestEntity_count_check == 1:
            print("check function called once")
        elif self.TestEntity.TestEntity_count_check > 1:
            print("check function called", self.TestEntity.TestEntity_count_check, "times")
        if self.TestEntity.TestEntity_count_error == 0:
            count = 0
            for i in range(len(self.data)):
                if self.data[i] != None:
                    count += 1
            return count
        else:
            return -1
