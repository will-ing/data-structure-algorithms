from challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter
import pytest


def test_animal():
    animal = AnimalShelter()
    animal.enqueue('dog', 'fido')
    assert animal.dog[0] == 'fido'


def test_enqueue_cat():
    animal = AnimalShelter()
    animal.enqueue('dog', 'fido')
    animal.enqueue('cat', 'fluffy')
    assert animal.dog[0] == 'fido'
    assert animal.cat[0] == 'fluffy'


def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('dog', 'fido')
    animal.enqueue('dog', 'rocket')
    animal.dequeue('dog')
    assert animal.dog[0] == 'fido'
