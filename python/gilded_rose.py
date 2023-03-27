# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if self._is_aged_brie(item):
                self.update_aged_brie(item)
            elif self._is_backstage_pass(item):
                self.update_backstage_passes(item)
            elif self._is_sulfuras(item):
                self.update_sulfuras(item)
            else:
                self.update_normal_items(item)

    def _is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def _is_backstage_pass(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def _is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        item.quality = min(item.quality, 50)
        item.sell_in -= 1

    def update_sulfuras(self, item):
        pass

    def update_normal_items(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
