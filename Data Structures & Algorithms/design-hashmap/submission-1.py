class MyHashMap:

    def __init__(self):
        self.data = []   # store [key, value] pairs

    def put(self, key: int, value: int) -> None:
        # update if key already exists
        for pair in self.data:
            if pair[0] == key:
                pair[1] = value
                return

        # otherwise insert new pair
        self.data.append([key, value])

    def get(self, key: int) -> int:
        # search for key
        for k, v in self.data:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        # find and delete the pair
        for i in range(len(self.data)):
            if self.data[i][0] == key:
                self.data.pop(i)
                return


