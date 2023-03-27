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

    def _increase_quality(self, item, amount=1):
        item.quality = min(item.quality + amount, 50)

    def _decrease_quality(self, item, amount=1):
        item.quality = max(item.quality - amount, 0)

    def _decrease_sell_in(self, item, amount=1):
        item.sell_in = (item.sell_in - amount)

    def _is_quality_max(self, item):
        return item.quality < 50
    
    def _is_quality_min(self, item):
        return item.quality > 0
    
    def _is_sell_in_negative(self, item):
        return item.sell_in < 0

    def _is_expired(self, item):
        return item.sell_in < 0

    def update_aged_brie(self, item):
        self._decrease_sell_in(item)
        if self._is_quality_max(item):
            self._increase_quality(item)
        if self._is_sell_in_negative(item) and self._is_quality_max(item):
            self._increase_quality(item)

    def update_backstage_passes(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            self._increase_quality(item, amount=3)
        elif item.sell_in <= 10:
            self._increase_quality(item, amount=2)
        else:
            self._increase_quality(item)
        self._decrease_sell_in(item)

    def update_sulfuras(self, item):
        pass

    def update_normal_items(self, item):
        if self._is_quality_min(item):
            self._decrease_quality(item)
        self._decrease_sell_in(item)
        if self._is_expired(item) and self._is_quality_min(item):
            self._decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
