class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node


class LinkedList:

    def __init__(self):
        self.head = None

    def get_head_node(self):
        return self.head

    def add_node(self, value):

        new_node = Node(value)

        if self.get_head_node() == None:
            self.head = new_node

        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        
    def get_head_value(self):
        if self.head is None:
            return None
        
        return self.get_head_node().get_value()


class HashMap:

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def my_hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code + count_collisions

    def compressor(self, hash_code):

        return hash_code % self.array_size

    def assign(self, key, value):

        array_index = self.compressor(self.my_hash(key))
        current_array_value_at_idx = self.array[array_index]

        if current_array_value_at_idx is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value_at_idx[0] == key:
            self.array[array_index] = [key, value]
            return

        number_of_collisions = 1

        while current_array_value_at_idx[0] != key:

            new_hash_code = self.my_hash(key, number_of_collisions)
            new_idx = self.compressor(new_hash_code)
            current_array_value_at_idx = self.array[new_idx]

            if current_array_value_at_idx is None or current_array_value_at_idx[0] == key:
                self.array[new_idx] = [key, value]
                return

            number_of_collisions += 1
        return

    def retrieve(self, key):

        array_idx = self.compressor(self.my_hash(key))
        possible_return = self.array[array_idx]

        if possible_return is None:
            return None

        if possible_return[0] == key:
            return possible_return[1]

        number_of_collisions = 1

        while possible_return[0] != key:

            new_hash_code = self.my_hash(key, number_of_collisions)
            new_idx = self.compressor(new_hash_code)
            possible_return = self.array[new_idx]

            if possible_return is None:
                return None

            if possible_return[0] == key:
                return possible_return[1]
            
            number_of_collisions += 1

        return
