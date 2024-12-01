import pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.parametrize('input, result', [("volodya","Volodya"),
                                           ("453","453"),
                                           ("good day","Good day"),
                                           ])
def test_capitilize_positive(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result

@pytest.mark.parametrize('input, result', [("", ""),
                                           (" ", " "),
                                               ('None', 'None')])
def test_capitilize_negative(input, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(input)
    assert res == result

@pytest.mark.parametrize('input, result', [(" привет","привет"),
                                           (" 545", "545"),
                                           (" world", "world")
                                           ])
def test_trim_positive(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result

@pytest.mark.parametrize('input, result', [(" ", ""),
                                           ('None','None'),
                                           (" mo bi le", "mo bi le")
                                           ])
def test_trim_negative(input, result):
    string_utils = StringUtils()
    res = string_utils.trim(input)
    assert res == result

@pytest.mark.parametrize('input, delemiter, result', [
                        ("1, 2, 3", ",", ["1", " 2", " 3"]),
             ("мир, труд, май", ",", ["мир", " труд", " май"])
    ])
def test_to_list_positive(input, delemiter, result):
    string_utils = StringUtils()
    res = string_utils.to_list(input, delemiter)
    assert res == result

@pytest.mark.parametrize('input, delemiter, result', [
    ("", ",", []),
    ("", None, [])
])
def test_to_list_negative(input, delemiter, result):
    string_utils = StringUtils()
    if delemiter is None:
        res = string_utils.to_list(input)
    else:
        res = string_utils.to_list(input, delemiter)
    assert res == result

@pytest.mark.parametrize('input, symbol', [("Skypro", "S"),
                                           ("Владимир", "В")])
def test_contains_positive(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == True

@pytest.mark.parametrize('input, symbol', [("Moscow", "S"),
                                           ("Dark", "R")])
def test_contains_negative(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == False

@pytest.mark.parametrize('input, symbol, result ', [("Skypro", "o", "Skypr"),
                                           ("Праздник", "д", "Празник"),
                                            ("Сонник", "ник", "Сон")
                                           ])
def test_delete_simbol_positive(input, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input, symbol)
    assert res == result

@pytest.mark.parametrize('input, symbol, result ', [("", "", ""),
                                           (" ", " ", "")
                                                    ])
def test_delete_simbol_negative(input, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(input, symbol)
    assert res == result

@pytest.mark.parametrize('input, symbol', [("Skypro", "S"),
                                           ("Владимир", "В")])
def test_starts_with_positive(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == True

@pytest.mark.parametrize('input, symbol', [("Moscow", "R"),
                                           ("Dark", "W")])
def test_starts_with_negative(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == False

@pytest.mark.parametrize('input, symbol', [("Skypro", "o"),
                                           ("Владимир", "р")])
def test_end_with_positive(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == True

@pytest.mark.parametrize('input, symbol', [("Moscow", "v"),
                                           ("Dark", "f")])
def test_end_with_negative(input, symbol):
    res = StringUtils()
    assert res.contains(input, symbol) == False

@pytest.mark.parametrize('input, is_empty', [("Skypro", ""),
                                           (" Home", " ")])
def test_is_empty_positive(input, is_empty):
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty(" ") == True

@pytest.mark.parametrize('input, is_empty', [("Moscow", "Moscow"),
                                           ("765", "765")])
def test_is_empty_negative(input, is_empty):
    assert string_utils.is_empty("Moscow") == False
    assert string_utils.is_empty("765") == False

@pytest.mark.parametrize('input, joiner, result', [([1,2,3,4], ", ", "1, 2, 3, 4"),
                                                   (["Sky", "Pro"], ", ", "Sky, Pro"),
                                                    (["Sky", "Pro"], "-", "Sky-Pro")
                                                   ])
def test_list_to_string_positive(input, joiner, result):
    string_utils = StringUtils()
    res = string_utils.list_to_string(input, joiner)
    assert res == result

@pytest.mark.parametrize('input, joiner, result', [([], ", ", ""),
                                                   ([], None, "")
                                                   ])
def test_list_to_string_negative(input, joiner, result):
    string_utils = StringUtils()
    if joiner is None:
        res = string_utils.list_to_string(input)
    else:
        res = string_utils.list_to_string(input, joiner)
    assert res == result