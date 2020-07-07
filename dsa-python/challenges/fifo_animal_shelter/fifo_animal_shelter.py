class AnimalShelter():
    """
    animal shelter class
    """

    def __init__(self):
        self.dog = []
        self.cat = []

    def enqueue(self, animal, name):
        if animal == 'dog':
            self.dog.append(name)
        elif animal == 'cat':
            self.cat.append(name)
        else:
            raise ValueError('enter cat or dog animals')

    def dequeue(self, pref):
        if pref == 'cat':
            return self.cat.pop()
        elif pref == 'dog':
            return self.cat.pop()
        else:
            raise ValueError('enter cat or dog animals')
