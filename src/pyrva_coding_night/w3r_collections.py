# https://www.w3resource.com/python-exercises/collections/
from typing import Dict, List, Tuple
import collections


def print_by_count(char_counts: Dict[str, int]) -> List[str]:
    my_tally = collections.Counter(**char_counts)
    return list(my_tally.elements())


def get_most_common_chars(my_string: str) -> List[Tuple[str, int]]:
    my_tally = collections.Counter(my_string)
    return my_tally.most_common(3)


