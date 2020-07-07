class AnimalShelter():
    """
    animal shelter class
    """

    def __init__(self):
        self.dog = []
        self.cat = []

    def enqueue(self, animal, name):
        """
        Adds animal and name to a stack

        Args:
            animal (string): [Dog or Cat]
            name (string): [Any]

        Raises:
            ValueError: [If not dog or cat is entered]
        """
        if animal == 'dog':
            self.dog.append(name)
        elif animal == 'cat':
            self.cat.append(name)
        else:
            raise ValueError('enter cat or dog animals')

    def dequeue(self, pref):
        """
        This removes the animal out of the shelter

        Args:
            pref (string): cat or dog

        Raises:
            ValueError: If cat or dog is not entered return error
        """
        if pref == 'cat':
            self.cat.pop()
        elif pref == 'dog':
            self.dog.pop()
        else:
            raise ValueError('enter cat or dog animals')
