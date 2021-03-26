import pytest

from tests.conftest import w3r_collections


@pytest.mark.parametrize('char_counts,expected', [
    ({'p': 4, 'q': 2, 'r': 0, 's': -2}, ['p', 'p', 'p', 'p', 'q', 'q'])
])
def test_print_by_count(char_counts, expected):
    assert w3r_collections.print_by_count(char_counts) == expected


@pytest.mark.parametrize('my_string,expected', [
    ('lkseropewdssafsdfafkpwe', [('s', 4), ('e', 3), ('f', 3)])
])
def test_get_most_common_chars(my_string, expected):
    assert w3r_collections.get_most_common_chars(my_string) == expected
