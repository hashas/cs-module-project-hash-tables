class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.data = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        node = self.data[index]

        # check if there is a head node
        if node is None:
            self.data[index] = new_entry
            self.count += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)

        else:
            # walk the linked list to check for same key
            cur = self.data[index]
            while cur:
                if cur.key == key:
                    cur.value == value
                    self.count += 1
                    if self.get_load_factor() > 0.7:
                        self.resize(self.capacity * 2)
                    break
                # if key's don't match, move the cur pointer to next node
                elif cur.next:
                    cur = cur.next
                else:
                    cur.next = new_entry
                    self.count += 1
                    if self.get_load_factor() > 0.7:
                        self.resize(self.capacity * 2)

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
        
        # if there's no node
        if node is None:
            print(f'WARNING! Key is not found')

        # special case: head node 
        # matching head with no next
        if node.key == key and node.next is None:
            self.data[index] = None
            self.count -= 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        # matching head with a next
        if node.key == key:
            self.data[index] = node.next
            self.count -= 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        # head doesn't match
        else:
            cur = self.data[index]
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    cur = None
                    self.count -= 1
                    if self.get_load_factor() > 0.7:
                        self.resize(self.capacity * 2)
                elif cur.next:
                    prev = cur
                    cur = cur.next
                else:
                    cur = None
                    print(f'WARNING! Key is not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
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

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_ht = HashTable(new_capacity)

        for i in range(self.capacity):
            curr_node = self.data[i]

            while curr_node is not None:
                # new_ht.data.insert(curr_node.key, curr_node.value)
                # new_ht.data.insert(i, curr_node)
                new_ht.put(curr_node.key, curr_node.value)
                curr_node = curr_node.next

        self.data = new_ht.data
        self.capacity = new_ht.capacity




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
