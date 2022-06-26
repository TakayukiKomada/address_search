import unittest
from search_address import search_address


class MyTestCase(unittest.TestCase):
    def test_有分番号を住所から取得できる_0287302(self):
        postal_code = "0287302"
        address = search_address(postal_code)
        expect = "岩手県八幡平市八幡平温泉郷"
        self.assertEqual(expect, address)

    unittest.main()


