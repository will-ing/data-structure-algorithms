from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation
import pytest


def test_proof_of_life():
    assert 5 == 5


def test_is_string():
    assert multi_bracket_validation(3) == False


def test_recognize_curly():
    assert multi_bracket_validation('()') == True


def test_recognize_square():
    assert multi_bracket_validation('[]') == True


def test_recognize_multi_braces():
    assert multi_bracket_validation('([])') == True


def test_recognize_multi_braces_code():
    assert multi_bracket_validation('([code])') == True


def test_recognize_multi_all():
    assert multi_bracket_validation('({[]})') == True


def test_recognize_nested_wrong():
    assert multi_bracket_validation('([)])') == False


def test_recognize_nested_wrong_two():
    assert multi_bracket_validation('[{(9(}]') == False
