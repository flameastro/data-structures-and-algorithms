class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.occupied = 0

    def _hash(self, key):
        LETTERS = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        hash_value = 432

        for letter in key.lower():
            if letter in LETTERS:
                hash_value += LETTERS.index(letter) * 2 + (LETTERS.index(letter) * 4)
            else:
                if letter.isnumeric():
                    hash_value *= 43

        return hash_value % self.size

    def insert(self, key, value, table=None):
        self.resize()

        if not table:
            table = self.table

        index = self._hash(key)
        found = False

        bucket = table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                found = True
                break

        if found:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
            self.occupied += 1

        return table

    def get(self, key):
        index = self._hash(key)
        result = None

        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                result = item[1]
                break

        return result

    def remove(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                self.occupied -= 1
                break

    def resize(self):
        percentage = self.occupied / self.size

        if percentage > 0.7:
            old_table = self.table

            self.size *= 2
            self.table = [[] for _ in range(self.size)]

            old_occupied = self.occupied
            self.occupied = 0

            for bucket in old_table:
                for key, value in bucket:
                    self.insert(key, value)

            self.occupied = old_occupied


hashtable = HashTable(10)
