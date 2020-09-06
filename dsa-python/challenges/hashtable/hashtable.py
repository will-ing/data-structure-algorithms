from challenges.linked_list.linked_list import Node, LinkedLists


class Hashtable:
    """
    Class for making a hashtable
    """

    def __init__(self, size=1024):
        """
        Args:
            size (int, optional): Size of the hashtable. Defaults to 1024.
        """
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """
        Converts key to a number to be stored.

        Args:
            key (type): any value

        Returns:
            int: the converted key to be stored
        """
        hash_ttl = 0

        for char in key:
            hash_ttl += ord(char)

        return (hash_ttl * 199) % self.size

    def add(self, key, value):
        """
        add a linkedlist to the hashtable bucket

        Args:
            key (any): any value
            value (any): int, str, list, dict
        """
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedLists()

        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        """
        Get the value of the key

        Args:
            key (any): int or str

        Returns:
            value (any): int, str, list, dict
        """
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head

        while current:
            if current.data[0] == key:
                return current.data[1]
            elif current.data[0] == None:
                return 'does not exist'
            current = current.next_node

    def contatins(self, key):
        """
        Returns a boolean if key exists in the hashtable

        Args:
            key (any): int or str

        Returns:
            bool: True or False
        """
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head

        while current:
            if current.data[0] == key:
                return True
            current = current.next_node
        return False
