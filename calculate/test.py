from .source import reverse_string


def test_should_reverse_string():
    assert reverse_string('abc') == 'cba'
