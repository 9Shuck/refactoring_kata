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
    
    # [quality > 0 && sell_in > 0]
    def test_normal_quality(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(39, items[0].quality)

    # [quality > 0 && sell_in > 0]
    def test_normal_sell_in(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)

    # [quality = 0 && sell_in = 0]
    def test_normal_quality_null(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    # [quality = 0 && sell_in = 0]
    def test_normal_sell_in_null(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    # [quality > 0 && sell_in = 0]
    def test_normal_quality_no_sell(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    # [quality > 0 && sell_in = 0]
    def test_normal_sell_in_no_sell(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)


    # AGED BRIE TESTING

    # [quality > 0 && quality < 50]
    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(41, items[0].quality)

    # [quality = 50]
    def test_aged_brie_quality_max(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
    
    # [quality = 50]
    def test_aged_brie_sell_in_max(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
    
    # [quality = 50]
    def test_aged_brie_quality_negative(self):
        items = [Item("Aged Brie", -2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(42, items[0].quality)


    # SULFURAS TESTING

    # [No changes should be applied]
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(40, items[0].quality)
    
    # [No changes should be applied]
    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(40, items[0].quality)


    # BACKSTAGE TESTING
    
    # [sell_in > 10]
    def test_backstage_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(36, items[0].quality)
    
    # [sell_in = 10]
    def test_backstage_quality_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)
    
    # [sell_in < 10 && sell_in > 5]
    def test_backstage_quality_seven(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)
    
    # [sell_in = 5]
    def test_backstage_quality_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)

    # [sell_in < 5 && sell_in > 0]
    def test_backstage_quality_three(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(38, items[0].quality)
    
    # [sell_in < 0]
    def test_backstage_quality_negative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -2, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
    
    # [Testing quality exceeded]
    def test_backstage_quality_exceeded(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 60)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        
    # [Testing sell_in output]
    def test_backstage_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(14, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
