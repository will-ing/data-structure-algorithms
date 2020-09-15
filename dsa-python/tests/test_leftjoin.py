from challenges.left_join.left_join import left_join
from challenges.hashtable.hashtable import Hashtable


def test_left():
    hashtable1 = Hashtable()
    hashtable2 = Hashtable()
    hashtable1.add('tired', 1)
    hashtable2.add('tired', 2)
    left_join(hashtable1, hashtable2)
    assert hashtable1.get('tired') == 1
