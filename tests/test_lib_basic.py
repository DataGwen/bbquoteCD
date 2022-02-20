from bbquoteCD.lib import get_quote

def test_get_quote_basic():
    assert get_quote() != ""