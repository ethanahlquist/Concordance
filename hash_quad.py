# -*- coding: utf-8 -*-
class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=0):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = (key, [value])
            self.num_items += 1
        elif self.hash_table[index][0] == key:
            self.hash_table[index][1].append(value)

        if self.get_load_factor() > 0.5:

            keys_and_vals = []
            for i in range(len(self.hash_table)):
                if self.hash_table[i] is None:
                    pass
                else:
                    keys_and_vals.append(self.hash_table[i])

            self.table_size = (2 * self.table_size) + 1
            self.num_items = 0
            self.hash_table = [None] * self.table_size

            for i in range(len(keys_and_vals)):
                for j in range(len(keys_and_vals[i][1])):
                    self.insert(keys_and_vals[i][0], keys_and_vals[i][1][j])


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

        n = min(len(key), 8)
        i = 0
        result = 0
        while i < n:
            result = ord(key[i]) + (31 * result)
            i += 1

        index = result % self.table_size
        return_val = index

        for i in range(1, self.table_size):
            #if i == self.table_size:
            #    return None

            if self.hash_table[return_val] is None:
                break
            elif self.hash_table[return_val][0] == key:
                break
            else:
                return_val = (index + i*i) % (self.table_size)

        return return_val


    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""

        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            return False
        #elif self.hash_table[index][0] != key:
        #    return False
        else:
            return True



    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""

        index = self.horner_hash(key)

        if self.hash_table[index] is None:
            return None
        #elif self.hash_table[index][0] != key:
        #    return None
        else:
            return index



    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        list_of_keys = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is None:
                pass
            else:
                list_of_keys.append(self.hash_table[i][0])
        return list_of_keys



    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""

        index = self.horner_hash(key)
        if self.hash_table[index] is None:
            return None
        #elif self.hash_table[index][0] != key:
        #    return None
        else:
            return self.hash_table[index][1]


    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items


    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size



    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

