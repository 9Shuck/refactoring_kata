# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("bread", items[0].name)

    # NORMAL ITEMS TEST
    
    def test_normal_quality(self):
        # [quality > 0 && sell_in > 0]
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    def test_normal_sell_in(self):
        # [quality > 0 && sell_in > 0]
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)

    def test_normal_quality_null(self):
        # [quality = 0 && sell_in = 0]
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_normal_sell_in_null(self):
        # [quality = 0 && sell_in = 0]
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    def test_normal_quality_no_sell(self):
        # [quality > 0 && sell_in = 0]
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    def test_normal_sell_in_no_sell(self):
        # [quality > 0 && sell_in = 0]
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    # AGED BRIE TESTING

    def test_aged_brie_quality(self):
        # [quality > 0 && quality < 50]
        items = [Item("Aged Brie", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(41, items[0].quality)

    def test_aged_brie_quality_max(self):
        # [quality = 50]
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
    
    def test_aged_brie_sell_in_max(self):
        # [quality = 50]
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
    
    def test_aged_brie_quality_negative(self):
        # [quality = 50]
        items = [Item("Aged Brie", -2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(42, items[0].quality)

    # SULFURAS TESTING

    def test_sulfuras_quality(self):
        # [No changes should be applied]
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(40, items[0].quality)
    
    def test_sulfuras_sell_in(self):
        # [No changes should be applied]
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(40, items[0].quality)

    # BACKSTAGE TESTING
    
    def test_backstage_quality(self):
        # [sell_in > 10]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(36, items[0].quality)
    
    def test_backstage_quality_ten(self):
        # [sell_in = 10]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)
    
    def test_backstage_quality_seven(self):
        # [sell_in < 10 && sell_in > 5]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)
    
    def test_backstage_quality_five(self):
        # [sell_in = 5]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    def test_backstage_quality_three(self):
        # [sell_in < 5 && sell_in > 0]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)
    
    def test_backstage_quality_negative(self):
        # [sell_in < 0]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -2, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
    
    def test_backstage_quality_exceeded(self):
        # [Testing quality exceeded]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 60)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        
    def test_backstage_sell_in(self):
        # [Testing sell_in output]
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(14, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
