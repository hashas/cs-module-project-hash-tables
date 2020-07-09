class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.data = [None] * capacity
        self.count = 0

    def djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        node = self.data[index]

        # check if there is a head node
        if node is None:
            self.data[index] = new_entry

        else:
            # walk the linked list to check for same key
            cur = self.data[index]
            while cur:
                if cur.key == key:
                    cur.value == value
                    break
                # if key's don't match, move the cur pointer to next node
                elif cur.next:
                    cur = cur.next
                else:
                    cur.next = new_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.data[index]
        prev = None

        # special case: head no next
        if node and node.next is None:
            self.data[index] = None
        
        if cur.key == key:
            cur = cur.next

        while cur:
            if cur.key == key:
                prev.next = cur.next
            else:
                prev = cur
                cur = cur.next

        print(f'WARNING! Key is not found')

        # self.put(key, None)


    def get(self, key):
        index = self.hash_index(key)
        node = self.data[index]

        if node is not None:
            cur = self.data[index]
            while cur:
                if cur.key == key:
                    return cur.value
                else:    
                    cur = cur.next
        else:
            return None
            
if __name__ == "__main__":
    ht = HashTable(8)
    
        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")
        
        ht.delete("key-7")
        return_value = ht.get("key-0")
        print(return_value is None)
        

        
        
