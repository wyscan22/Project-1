from SKEssentials.Main.MainII import is_list_or_tuple

import math
from abc import ABC, abstractmethod

class Box(ABC):
    @abstractmethod
    def __init__(self, *items):
        self.items = list(items)
        pass

    def item_count(self):
        return len(self.items)

    def add(self, *items):
        pass
    def remove(self, *items):
        pass

    def empty(self) -> tuple:
        items = tuple(self.items)
        if type(self.items) == dict:
            items = (e for k, e in self.items.items())
        self.items.clear()
        return items

    def __str__(self):
        string = "["
        if type(self.items) == dict:
            for k, item in self.items.items():
                string += f"\n    {str(k)} : {str(item)}"
        else:
            for item in self.items:
                string += f"\n    {str(item)}"
        string += "\n]"
        return string

class ListBox(Box):
    def __init__(self, *items):
        super().__init__(*items)

    def add(self, *items):
        self.items += items
    def remove(self, *items):
        for i, item in enumerate(self.items):
            if item in items:
                self.items.pop(i)
    def pop(self, *indicies):
        for index in indicies:
            self.items.pop(index)

class DictBox(Box):
    def __init__(self, *items):
        _dict = {}
        for i, item in enumerate(items):
            if is_list_or_tuple(item):
                _dict[item[0]] = item[1]
            else:
                _dict[i] = item
        self.items = _dict

    def add(self, key, item):
        try:
            _ = self.items[key]
        except KeyError:
            self.items[key] = item
    def remove(self, item):
        key = next((k for k, e in self.items.items() if e == item), None)
        self.items.pop(key)
    def pop(self, key):
        self.items.pop(key)

class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return (
            f"{self.name} [Value: {self.value}]"
        )

def repack_boxes(*boxes):
    items = []
    for box in boxes: # Unpack Items
        assert isinstance(box, Box), f"{box} is not a Box."
        items += box.items
        box.empty()

    a = math.ceil(len(items) / len(boxes))
    b = len(items) % len(boxes)
    c_idx = 0

    for i in range(len(boxes)):
        if i == b - 1: a -= 1
        for j in range(a):
            if isinstance(boxes[i], DictBox):
                boxes[i].add(c_idx, items[c_idx])
            else:
                boxes[i].add(items[c_idx])
            c_idx += 1


# Example

Box1 = ListBox(*(n for n in range(20)))
Box2 = ListBox(*(n for n in range(9)))
Box3 = DictBox(*((chr(n + 64), Item("Item " + str(n), 100 * n)) for n in range(13)))

repack_boxes(Box1, Box2, Box3)

print("Box1 =", Box1)
print("Box2 =", Box2)
print("Box3 =", Box3)