"""
Create a simple hashtable
"""

class Node():
    """value Node for Hashtable values
    """
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable(object):
    
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.table = [None]*capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def set_key(self, key, value):
        index = self._hash(key)

        current_item = self.table[index]

        if not current_item:
            self.table[index] = Node(key, value)
        
        while current_item:
            if current_item.key == key:
                current_item.value = value
                return
            
            if current_item.next:
                current_item = current_item.next
            else:
                current_item.next = Node(key, value)
                
    def get_key(self, key):
        index = self._hash(key)

        current_item = self.table[index]
        while current_item:
            if current_item.key == key:
                return current_item.value
            
            if current_item.next:
                current_item = current_item.next
            else:
                raise KeyError


if __name__=="__main__":
    hash_table = Hashtable()

    hash_table.set_key("name", "david")
    hash_table.set_key("job", "developer")

    assert hash_table.get_key("name")=="david"
    assert hash_table.get_key("job")=="developer"