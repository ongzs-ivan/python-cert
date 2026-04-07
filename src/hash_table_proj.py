class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        hash_sum = 0
        for char in string:
            hash_sum += ord(char)
        return hash_sum

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]

if __name__ == "__main__":
    # test run
    hashtable = HashTable()
    hashtable.add('shape','square')
    print(hashtable.lookup('shape'))
    hashtable.remove('square')