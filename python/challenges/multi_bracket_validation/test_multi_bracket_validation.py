from multi_bracket_validation import multi_bracket_validation

def test_func_exists():
    multi_bracket_validation('')

def test_balanced():
    s = "{}"
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_balanced_big():
    s = "{}(){}"
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_balanced_xtrachars():
    s = "()[[Extra Characters]]"
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_balanced_nested():
    s = "(){}[[]]"
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_balanced_nested_text():
    s = "{}{Code}[Fellows](())"
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_unbalanced():
    s = "[({}]"
    expected = False
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_unbalanced_short1():
    s = "(]("
    expected = False
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_unbalanced_short2():
    s = "{(})"
    expected = False
    actual = multi_bracket_validation(s)
    assert expected == actual

def test_empty():
    s = ""
    expected = True
    actual = multi_bracket_validation(s)
    assert expected == actual

"""
- [ ] Balanced
- [ ] Balanced Complicated
- [ ] Balanced extra characters
- [ ] Balanced nested
- [ ] Balanced alternating
- [ ] Unbalanced
- [ ] Only Open
- [ ] Only Closed
- [ ] Empty
"""
