import unittest

from bbquoteCD.lib import get_quote

class TestbbquoteLib(unittest.TestCase):
    def test_get_quote_length(self):
        self.assertNotEqual(get_quote(),"")
    