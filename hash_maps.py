# Hash tables map key to value using a hash function Big O(1)
# hash function takes the key and do MOD operation form the sum of ASCII values 
# Collision happens when tow keys have the same hash values:
#  - Chaining: we create a link list of values that have the same hash ---> might go to Big O(n)
#  - Linear probling: searching for an empty spot to store the new value

class HashTable():
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for c in key:
            h +=ord(c)
        return h%self.max

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    # more suitable for dictionary
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # linkedlist for collision 
        found = 0
        for idx, elm in enumerate(self.arr[h]):
            if len(elm)==2 and elm[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break
            if not found:
                self.arr[h].append((key, value))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        # linkedlist for collision
        for elm in self.arr[h]:
            if elm[0] == key:
                return elm[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        # linkedlist for collision
        for idx, elm in enumerate(self.arr[h]):
            if elm[0] == key:
                del self.arr[h][idx]

t = HashTable()
print(t.get_hash('march 6'))
t.add('march 6', 30)
print(t.get('march 6'))

t['march 5'] = 95
print(t['march 5'])
