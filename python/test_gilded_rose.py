# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("bread", items[0].name)

    # Test update_normal_items().quality [quality > 0 && sell_in > 0]
    def test_normal_quality(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    # Test update_normal_items().sell_in [quality > 0 && sell_in > 0]
    def test_normal_sell_in(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)

    # Test update_normal_items().quality [quality = 0 && sell_in = 0]
    def test_normal_quality_null(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    # Test update_normal_items().sell_in [quality = 0 && sell_in = 0]
    def test_normal_sell_in_null(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    # Test update_normal_items().sell_in [quality > 0 && sell_in = 0]
    def test_normal_quality_no_sell(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    # Test update_normal_items().sell_in [quality > 0 && sell_in = 0]
    def test_normal_sell_in_no_sell(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
