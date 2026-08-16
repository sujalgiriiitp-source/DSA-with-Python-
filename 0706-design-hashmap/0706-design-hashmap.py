class MyHashMap:

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return