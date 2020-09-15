from challenges.hashtable.hashtable import Hashtable


def left_join(left, right):
    """
    joins hashtabels together

    Args:
        left (hashtable): a hashtable that consists of linkedlists
        right (hashtable): a hashtable that consists of linkedlists

    Returns:
        hashtable: Returns a hash table with combined left and right
    """
    if left._buckets == None:
        return False

    current = left._buckets.head

    while current:

        if right.contains(current.data[0]):
            left.add(current.data[0], right.get(current))
        else:
            left.add(right.head.data[0], right.get(current))
        current = current.next_node
